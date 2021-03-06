# -*- coding: utf-8 -*-

# Copyright 2019 The GraphicsFuzz Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Processes coverage files."""

import io
import os
import subprocess
import threading
import typing
from collections import Counter
from queue import Queue
from typing import Dict, List, Tuple

from attr import dataclass

# Type:
from gfauto import util

LineCounts = Dict[str, typing.Counter[int]]

DirAndItsFiles = Tuple[str, List[str]]

DirAndItsOutput = Tuple[str, str]

IGNORED_MISSING_FILES = ["CMakeCXXCompilerId.cpp", "CMakeCCompilerId.c"]


@dataclass  # pylint: disable=too-many-instance-attributes;
class GetLineCountsData:
    gcov_path: str
    gcov_uses_json_output: bool
    build_dir: str
    gcov_prefix_dir: str
    num_threads: int
    gcda_files_queue: "Queue[DirAndItsFiles]" = Queue()
    stdout_queue: "Queue[DirAndItsOutput]" = Queue()
    line_counts: LineCounts = {}


def _thread_gcov(data: GetLineCountsData) -> None:
    # Keep getting files and processing until the special "done" ("", []) message.

    while True:
        root, files = data.gcda_files_queue.get()
        if not root:
            # This is the special "done" message.
            break
        cmd = [data.gcov_path, "-i"]
        if data.gcov_uses_json_output:
            cmd.append("-t")
        cmd.extend(files)
        # I.e.: cd $root && gcov -i -t file_1.gcda file_2.gcda ...
        result = subprocess.run(
            cmd,
            encoding="utf-8",
            errors="ignore",
            check=True,
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if data.gcov_uses_json_output:
            data.stdout_queue.put((root, result.stdout))
        else:
            gcov_files = [file + ".gcov" for file in files]
            gcov_contents = []
            for gcov_file in gcov_files:
                with open(
                    os.path.join(root, gcov_file),
                    "r",
                    encoding="utf-8",
                    errors="ignore",
                ) as f:
                    gcov_contents.append(f.read())
            gcov_contents_combined = "\n".join(gcov_contents)
            data.stdout_queue.put((root, gcov_contents_combined))


def _thread_gcovs(data: GetLineCountsData) -> None:
    threads = [
        threading.Thread(target=_thread_gcov, args=(data,))
        for _ in range(data.num_threads)
    ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # send "done" message to adder thread.
    data.stdout_queue.put(("", ""))


def _process_text_lines(data: GetLineCountsData, lines: typing.TextIO) -> None:
    current_file = ""
    current_file_line_counts: typing.Counter[int] = Counter()
    for line in lines:
        line = line.strip()
        # file:file_path
        if line.startswith("file:"):
            current_file = line[5:]
            current_file_line_counts = data.line_counts.setdefault(
                current_file, Counter()
            )
            continue
        # lcount:line number,execution_count,has_unexecuted_block
        if line.startswith("lcount:"):
            assert current_file
            line = line[7:]
            parts = line.split(sep=",")
            line_number = int(parts[0])
            count = int(parts[1])
            # Confusingly, |update| adds counts.
            current_file_line_counts.update({line_number: count})
            continue


def _process_json_lines(data: GetLineCountsData, lines: typing.TextIO) -> None:
    current_file = ""
    current_file_line_counts: typing.Counter[int] = Counter()
    # The count value given by the previous line, which may or may not be used depending on the next line.
    current_count = -1
    for line in lines:
        line = line.strip()
        # "file": "file_name",
        if line.startswith('"file": "'):
            assert current_count < 0
            current_file = line[9:-2]
            current_file_line_counts = data.line_counts.setdefault(
                current_file, Counter()
            )
            continue
        # "count": count,
        if line.startswith('"count": '):
            assert current_file
            current_count = int(line[9:-1])
            continue
        # "line_number": line_number,
        if line.startswith('"line_number": '):
            assert current_file
            assert current_count >= 0
            line_number = int(line[15:-1])
            # Confusingly, |update| adds counts.
            current_file_line_counts.update({line_number: current_count})
            # Fallthrough.

        # Reset current_count; the "count" field can occur in a few places, but we only want to use the count that
        # is immediately followed by "line_number".
        current_count = -1


def _thread_adder(data: GetLineCountsData) -> None:
    # Keep processing stdout entries until we get the special "done" message.

    while True:
        root, stdout = data.stdout_queue.get()
        if not root:
            # This is the special "done" message.
            break
        lines = io.StringIO(stdout)

        if data.gcov_uses_json_output:
            _process_json_lines(data, lines)
        else:
            _process_text_lines(data, lines)


def get_line_counts(data: GetLineCountsData) -> None:

    root: str
    files: List[str]

    # In gcov_prefix_dir, add symlinks to build_dir .gcno files.
    print("Adding symlinks.")

    # If the symlinks already exist, we will get an error.
    # os.symlink does not provide an option to overwrite.
    # We instead create the symlink with a randomized name and then rename it using os.replace, which atomically
    # overwrites any existing file.
    random_text = util.get_random_name()[:10]

    for root, _, files in os.walk(data.build_dir):
        gcno_files = [f for f in files if f.endswith(".gcno")]
        if gcno_files:
            root_rel = strip_root(root)
            os.makedirs(os.path.join(data.gcov_prefix_dir, root_rel), exist_ok=True)
            for file_name in gcno_files:
                source = os.path.join(root, file_name)
                dest = os.path.join(data.gcov_prefix_dir, root_rel, file_name)
                temp = dest + random_text
                os.symlink(source, temp)
                os.replace(temp, dest)

    print("Done.")

    print("Processing .gcno files.")

    gcovs_thread = threading.Thread(target=_thread_gcovs, args=(data,))
    adder_thread = threading.Thread(target=_thread_adder, args=(data,))

    gcovs_thread.start()
    adder_thread.start()

    for root, _, files in os.walk(
        os.path.join(data.gcov_prefix_dir, strip_root(data.build_dir))
    ):
        gcno_files = [f for f in files if f.endswith(".gcno")]
        # TODO: Could split further if necessary.
        if gcno_files:
            data.gcda_files_queue.put((os.path.join(root), gcno_files))

    # Send a "done" message for each thread.
    for _ in range(data.num_threads):
        data.gcda_files_queue.put(("", []))

    # wait for threads.
    gcovs_thread.join()
    adder_thread.join()

    print("Done.")


INDENT = 8


def strip_root(path: str) -> str:
    path_stripped = path
    if os.path.isabs(path_stripped):
        # Most of this coverage code only works on Linux, so we assume Linux here.
        # If we had Windows paths that could be on different drives etc., we would need to be more careful.
        util.check(
            path_stripped.startswith("/"),
            AssertionError(f"Non-posix absolute file path? {path}"),
        )
        path_stripped = path_stripped[1:]
    util.check(
        not path_stripped.startswith("/"),
        AssertionError(
            f"Internal error trying to make a relative path: {path_stripped}"
        ),
    )
    return path_stripped


def output_source_files(
    build_dir: str,
    output_dir: str,
    line_counts: LineCounts,
    force_zero_coverage: bool = False,
) -> None:
    build_dir = os.path.abspath(build_dir)

    for source_path, counts in line_counts.items():
        source_path = os.path.join(build_dir, source_path)
        source_path = os.path.normpath(source_path)

        if not os.path.isfile(source_path):
            if not os.path.basename(source_path) in IGNORED_MISSING_FILES:
                print(f"WARNING: Could not find source file: {source_path}")
            continue

        dest_path = os.path.join(output_dir, strip_root(source_path))

        with open(source_path, "r", encoding="utf-8", errors="ignore") as source_file:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, "w", encoding="utf-8", errors="ignore") as dest_file:
                line_number = 1
                while True:
                    line = source_file.readline()
                    if not line:
                        break
                    # .get() returns None if the line is not executable
                    line_count = counts.get(line_number)
                    if line_count:
                        if force_zero_coverage:
                            line_count = 0
                        line_count_str = str(line_count) + " "
                    else:
                        line_count_str = " "
                    line_count_str = (
                        " " * (INDENT - len(line_count_str)) + line_count_str
                    )
                    line = line_count_str + line
                    dest_file.write(line)
                    line_number += 1
