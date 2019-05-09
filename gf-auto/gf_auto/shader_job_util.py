

import pathlib
from typing import Iterable
import util


frag_ext = '.frag'
vert_ext = '.vert'
comp_ext = '.comp'

all_ext = (frag_ext, vert_ext, comp_ext)

glsl_suffix = ''
spirv_suffix = '.spv'
asm_spirv_suffix = '.asm'


glsl_shader_job_related_file_extensions = ['.frag', '.vert', '.comp']
spirv_shader_job_related_file_extensions = ['.frag.spv', '.vert.spv', '.comp.spv']
asm_spirv_shader_job_related_file_extensions = ['.frag.asm', '.vert.asm', '.comp.asm']


def shader_job_get_shader_contents_or_none(
    shader_job_file_path: pathlib.Path,
    extension: str,
    language_suffix: str = glsl_suffix,
):
    file = shader_job_file_path.with_suffix(extension + language_suffix)
    if file.exists():
        return util.file_read_text(file)

    return None


# Get related files.

def shader_job_get_related_files(
    shader_job_file_path: pathlib.Path,
    extensions: Iterable[str] = all_ext,
    language_suffix: str = glsl_suffix,
):
    # .frag, .comp, ...
    files = extensions

    # .frag.spv, .comp.spv
    files = [(f + language_suffix) for f in files]

    # variant_001.frag.spv, variant_001.comp.spv (does not exist), ...
    files = [shader_job_file_path.with_suffix(f) for f in files]

    # variant_001.frag.spv, ...
    files = [f for f in files if f.exists()]
    return files


# Copy files.


def shader_job_copy(
    shader_job_file_path: pathlib.Path,
    output_shader_job_file_path: pathlib.Path,
    extensions: Iterable[str] = all_ext,
    language_suffix: str = glsl_suffix,
):
    output_files = [output_shader_job_file_path]

    util.copy_file(shader_job_file_path, output_shader_job_file_path)

    # [source/variant.frag, source/variant.vert, ...]
    other_files = shader_job_get_related_files(shader_job_file_path, extensions, language_suffix)

    # [variant.frag, variant.vert, ...]
    dest_other_files = [f.name for f in other_files]

    # [dest/variant.frag, dest/variant.vert, ...]
    dest_other_files = [output_shader_job_file_path.with_name(f) for f in dest_other_files]

    for (source, dest) in zip(other_files, dest_other_files):
        util.copy_file(source, dest)
        output_files.append(dest)

    return output_files


