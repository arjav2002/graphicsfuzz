

import pathlib
import util
from typing import Optional, List

from shader_job_util import shader_job_copy
from util import tool_on_path, copy_file, file_mkdirs_parent
from subprocess_util import run
import re

#                      | group 1       ||g2|
pattern = re.compile(r'(void main\(\)\n)({)')


class AddRedPixelError(Exception):
    pass


def add_red_pixel_code_to_frag_file(
    frag_file: pathlib.Path
):
    frag_contents = util.file_read_text(frag_file)

    # Replace opening brace of main with the following.
    (frag_contents, n) = pattern.subn(r'''\1{
 if (gl_FragCoord.x < 10.0)
  {
   _GLF_color = vec4(1.0, 0.0, 0.0, 1.0);
   return;
  }''', frag_contents)

    if n != 1:
        raise AddRedPixelError(
            'Failed to add red pixel code using regex in {}'.format(str(frag_file))
        )

    util.file_write_text(frag_file, frag_contents)


def run_glsl_shader_job_add_red_pixels(
    input_shader_job_json_file_path: pathlib.Path,
    output_shader_job_json_file_path: pathlib.Path,
    graphics_fuzz_tool_path: Optional[pathlib.Path] = None,
) -> List[pathlib.Path]:

    if graphics_fuzz_tool_path:
        raise NotImplementedError(
            'Not yet implemented used of GraphicsFuzz to add red pixels to a shader'
        )

    output_files = shader_job_copy(
        input_shader_job_json_file_path,
        output_shader_job_json_file_path,
    )

    frag_files = [f for f in output_files if f.name.endswith('.frag')]

    if len(frag_files) != 1:
        raise FileNotFoundError(
            'Could not find single .frag file; found: {}'.format(frag_files)
        )

    frag_file = frag_files[0]

    add_red_pixel_code_to_frag_file(frag_file)

    return output_files