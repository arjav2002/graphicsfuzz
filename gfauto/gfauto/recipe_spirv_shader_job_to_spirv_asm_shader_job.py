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

import pathlib
from typing import List, Optional

from . import util
from .artifact_pb2 import ArtifactMetadata
from .artifacts import (
    Artifact,
    artifact_execute_recipe_if_needed,
    artifact_get_inner_file_path,
    artifact_write_metadata,
)
from .recipe_pb2 import RecipeSpirvShaderJobToSpirvAsmShaderJob
from .shader_job_util import shader_job_get_related_files, spirv_suffix
from .subprocess_util import run
from .util import tool_on_path


def run_spirv_dis_on_spirv_shader(
    input_spirv_file_path: pathlib.Path,
    output_dir_path: pathlib.Path,
    spirv_dis_file_path: Optional[pathlib.Path] = None,
) -> pathlib.Path:
    if not spirv_dis_file_path:
        spirv_dis_file_path = util.spirv_dis_on_path()

    output_spirv_file_path = output_dir_path / (
        util.remove_end(input_spirv_file_path.name, ".spv") + ".asm"
    )

    util.file_mkdirs_parent(output_spirv_file_path)

    run(
        [
            str(spirv_dis_file_path),
            str(input_spirv_file_path),
            "-o",
            str(output_spirv_file_path),
            "--raw-id",
        ]
    )

    return output_spirv_file_path


def run_spirv_shader_job_to_spirv_asm_shader_job(
    input_spirv_job_json_file_path: pathlib.Path,
    output_spirv_job_json_file_path: pathlib.Path,
    spirv_dis_file_path: Optional[pathlib.Path] = None,
) -> List[pathlib.Path]:

    if not spirv_dis_file_path:
        spirv_dis_file_path = util.spirv_dis_on_path()

    shader_files = shader_job_get_related_files(
        input_spirv_job_json_file_path, language_suffix=spirv_suffix
    )

    util.copy_file(input_spirv_job_json_file_path, output_spirv_job_json_file_path)

    output_shader_file_paths = []  # type: List[pathlib.Path]

    for shader_file in shader_files:
        asm_file_path = run_spirv_dis_on_spirv_shader(
            shader_file, output_spirv_job_json_file_path.parent, spirv_dis_file_path
        )
        output_shader_file_paths.append(asm_file_path)

    return output_shader_file_paths


def recipe_spirv_shader_job_to_spirv_asm_shader_job(
    recipe: RecipeSpirvShaderJobToSpirvAsmShaderJob, output_artifact_path: str
):
    artifact_execute_recipe_if_needed(recipe.spirv_shader_job_artifact)
    if len(recipe.spirv_dis_artifact) > 0:
        artifact_execute_recipe_if_needed(recipe.spirv_dis_artifact)

    # Wrap input artifact for convenience.
    input_artifact = Artifact(recipe.spirv_shader_job_artifact)

    output_metadata = ArtifactMetadata()
    output_metadata.data.spirv_asm_shader_job.spirv_job.CopyFrom(
        input_artifact.metadata.data.spirv_shader_job.spirv_job
    )

    output_metadata.derived_from.append(recipe.spirv_shader_job_artifact)
    if len(recipe.spirv_dis_artifact) > 0:
        output_metadata.derived_from.append(recipe.spirv_dis_artifact)

    input_json_path = artifact_get_inner_file_path(
        input_artifact.metadata.data.spirv_shader_job.spirv_job.shader_job_file,
        input_artifact.path,
    )

    output_json_path = artifact_get_inner_file_path(
        output_metadata.data.spirv_asm_shader_job.spirv_job.shader_job_file,
        output_artifact_path,
    )

    if len(recipe.spirv_dis_artifact) > 0:
        raise NotImplementedError("Not yet implemented the use of spirv_dis_artifact")

    spirv_dis_file_path = tool_on_path("spirv-dis")

    run_spirv_shader_job_to_spirv_asm_shader_job(
        input_json_path, output_json_path, spirv_dis_file_path
    )

    artifact_write_metadata(output_metadata, output_artifact_path)