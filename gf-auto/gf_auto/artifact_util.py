from typing import (
    Optional,
    List,
    Iterable,
)

import gf_logging
import util
import proto_util
from artifact_pb2 import ArtifactMetadata
from recipe_pb2 import (
    Recipe,
    RecipeGlslShaderJobToSpirvShaderJob,
    RecipeGlslShaderJobAddRedPixels,
    RecipeSpirvAsmShaderJobToAmberScript,
    RecipeSpirvShaderJobToSpirvAsmShaderJob,
    RecipeSpirvShaderJobToSpirvShaderJobOpt,
)
import pathlib
from run_glsl_shader_job_add_red_pixels import run_glsl_shader_job_add_red_pixels
from run_spirv_asm_shader_job_to_amber_script import run_spirv_asm_shader_job_to_amber_script
from run_spirv_opt import run_spirv_opt_on_spirv_shader_job
from run_spirv_shader_job_to_spirv_asm_shader_job import (
    run_spirv_shader_job_to_spirv_asm_shader_job
)
from util import tool_on_path
from run_glslang_spirv import run_glslang_glsl_to_spirv_job

artifact_metadata_file_name = 'artifact.json'
artifact_recipe_file_name = 'recipe.json'
artifact_recipe_log_file_name = 'recipe.log'


class Artifact:
    def __init__(self, path: str, metadata: ArtifactMetadata = None):
        self.path = path
        self.metadata = metadata
        if self.metadata is None:
            self.metadata = artifact_read_metadata(path)


class RecipeWrap:
    def __init__(self, path: str, recipe: Recipe = None):
        self.path = path
        self.recipe = recipe
        if self.recipe is None:
            self.recipe = artifact_read_recipe(path)


def artifact_path_to_path(artifact_path: str) -> pathlib.Path:
    """
    Returns |artifact_path| converted to an OS specific path.
    Artifact paths always use '/'.

    :param artifact_path: a path that uses '/'. Can be an "artifact name".
    :return:
    """

    # TODO: Consider Windows.
    return pathlib.Path(artifact_path)


def artifact_get_directory_path(artifact_path: str) -> pathlib.Path:
    return artifact_path_to_path(artifact_path)


def artifact_get_recipe_file_path(artifact_path: str) -> pathlib.Path:
    return artifact_get_inner_file_path(artifact_path, artifact_recipe_file_name)


def artifact_get_metadata_file_path(artifact_path: str) -> pathlib.Path:
    return artifact_get_inner_file_path(artifact_path, artifact_metadata_file_name)


def artifact_get_recipe_log_file_path(artifact_path: str) -> pathlib.Path:
    return artifact_get_inner_file_path(artifact_path, artifact_recipe_log_file_name)


def artifact_write_recipe(artifact_path: str, recipe: Recipe = Recipe()):
    json_text = proto_util.message_to_json(recipe, including_default_value_fields=True)
    json_file_path = artifact_get_recipe_file_path(artifact_path)
    util.file_write_text(json_file_path, json_text)
    return artifact_path


def artifact_read_recipe(artifact_path: str, recipe: Optional[Recipe] = None):
    if not recipe:
        recipe = Recipe()
    json_file_path = artifact_get_recipe_file_path(artifact_path)
    json_text = util.file_read_text(json_file_path)
    proto_util.json_to_message(json_text, recipe)
    return recipe


def artifact_write_metadata(
    artifact_path: str,
    artifact_metadata: ArtifactMetadata = ArtifactMetadata()
):
    json_text = proto_util.message_to_json(artifact_metadata, including_default_value_fields=True)
    json_file_path = artifact_get_metadata_file_path(artifact_path)
    util.file_write_text(json_file_path, json_text)


def artifact_read_metadata(
    artifact_path: str,
    artifact_metadata: Optional[ArtifactMetadata] = None
):
    assert len(artifact_path) > 0
    if not artifact_metadata:
        artifact_metadata = ArtifactMetadata()
    json_file_path = artifact_get_metadata_file_path(artifact_path)
    json_contents = util.file_read_text(json_file_path)
    proto_util.json_to_message(json_contents, artifact_metadata)
    return artifact_metadata


def artifact_execute_recipe_if_needed(artifact_path: str):
    artifact_execute_recipe(artifact_path, only_if_artifact_json_missing=True)


def artifact_execute_recipe(artifact_path: str, only_if_artifact_json_missing: bool = False):
    if only_if_artifact_json_missing and artifact_get_metadata_file_path(artifact_path).exists():
        return

    recipe = artifact_read_recipe(artifact_path)

    with util.file_open_text(artifact_get_recipe_log_file_path(artifact_path), 'w') as f:
        gf_logging.push_stream_for_logging(f)
        try:
            if recipe.HasField('glsl_shader_job_to_spirv_shader_job'):
                recipe_glsl_shader_job_to_spirv_shader_job_run(
                    artifact_path,
                    recipe.glsl_shader_job_to_spirv_shader_job,
                )
            elif recipe.HasField('spirv_shader_job_to_spirv_shader_job_opt'):
                recipe_spirv_shader_job_to_spirv_shader_job_opt_run(
                    artifact_path,
                    recipe.spirv_shader_job_to_spirv_shader_job_opt,
                )
            elif recipe.HasField('glsl_shader_job_add_red_pixels'):
                recipe_glsl_shader_job_add_red_pixels_run(
                    artifact_path,
                    recipe.glsl_shader_job_add_red_pixels,
                )
            elif recipe.HasField('spirv_shader_job_to_spirv_asm_shader_job'):
                recipe_spirv_shader_job_to_spirv_asm_shader_job_run(
                    artifact_path,
                    recipe.spirv_shader_job_to_spirv_asm_shader_job,
                )
            elif recipe.HasField('spirv_asm_shader_job_to_amber_script'):
                recipe_spirv_asm_shader_job_to_amber_script_run(
                    artifact_path,
                    recipe.spirv_asm_shader_job_to_amber_script,
                )
            else:
                raise NotImplementedError(
                    'Artifact {} has recipe type {} and this is not implemented'.format(
                        artifact_path,
                        recipe.WhichOneof('recipe'),
                    )
                )
        finally:
            gf_logging.pop_stream_for_logging()


def artifact_get_inner_file_path(artifact_path: str, inner_file: str) -> pathlib.Path:
    # TODO: Consider Windows.
    # TODO: Consider absolute paths that we might want to support for quick hacks.
    return artifact_get_directory_path(artifact_path) / pathlib.Path(inner_file)


# Type specific functions


def artifact_create_recipe_glslang_spv(artifact: str):
    recipe = Recipe()
    recipe.glsl_shader_job_to_spirv_shader_job.SetInParent()
    artifact_write_recipe(artifact, recipe)


def recipe_glsl_shader_job_to_spirv_shader_job_run(
    output_artifact_path: str,
    recipe: RecipeGlslShaderJobToSpirvShaderJob,
):
    artifact_execute_recipe_if_needed(recipe.glsl_shader_job_artifact)
    if len(recipe.glslang_validator_artifact) > 0:
        artifact_execute_recipe_if_needed(recipe.glslang_validator_artifact)

    # Inputs:  e.g. input_glsl_artifact/{x.json, x.frag, x.vert, ...}
    # Outputs: e.g. output_artifact/{x.json, x.frag.spv, x.vert.spv, ...}

    input_glsl_artifact_path = recipe.glsl_shader_job_artifact
    input_glsl_artifact_metadata = artifact_read_metadata(input_glsl_artifact_path)
    input_glsl_shader_job_path = artifact_get_inner_file_path(
        input_glsl_artifact_path,
        input_glsl_artifact_metadata.data.glsl_shader_job.shader_job_file
    )

    if len(recipe.glslang_validator_artifact) > 0:
        raise NotImplementedError('Not yet implemented the use of glslang_validator_artifact')

    glslang_validator_file_path = tool_on_path('glslangValidator')

    output_metadata = ArtifactMetadata()
    output_metadata.CopyFrom(input_glsl_artifact_metadata)
    output_metadata.data.spirv_shader_job.spirv_job.shader_job_file = (
        input_glsl_artifact_metadata.data.glsl_shader_job.shader_job_file
    )
    output_metadata.data.spirv_shader_job.spirv_job.red_pixel_at_top_left = \
        input_glsl_artifact_metadata.data.glsl_shader_job.red_pixel_at_top_left
    # Derived from.
    # TODO: This could be automated.
    output_metadata.derived_from.extend(input_glsl_artifact_metadata.derived_from)
    output_metadata.derived_from.append(recipe.glsl_shader_job_artifact)
    if len(recipe.glslang_validator_artifact) > 0:
        output_metadata.derived_from.append(recipe.glslang_validator_artifact)

    output_metadata.data.spirv_shader_job.spirv_job.glsl_shader_job_source_artifact = (
        input_glsl_artifact_path
    )

    output_shader_job_file_path = artifact_get_inner_file_path(
        output_artifact_path,
        output_metadata.data.spirv_shader_job.spirv_job.shader_job_file
    )

    run_glslang_glsl_to_spirv_job(
        input_glsl_shader_job_path,
        output_shader_job_file_path,
        glslang_validator_file_path,
    )

    artifact_write_metadata(output_artifact_path, output_metadata)


def recipe_spirv_shader_job_to_spirv_shader_job_opt_run(
    output_artifact_path: str,
    recipe: RecipeSpirvShaderJobToSpirvShaderJobOpt,
):
    artifact_execute_recipe_if_needed(recipe.spirv_shader_job_artifact)
    if len(recipe.spirv_opt_artifact) > 0:
        artifact_execute_recipe_if_needed(recipe.spirv_opt_artifact)

    # Wrap input artifact for convenience.
    input_spirv_artifact = Artifact(recipe.spirv_shader_job_artifact)

    output_metadata = ArtifactMetadata()
    output_metadata.CopyFrom(input_spirv_artifact.metadata)
    output_metadata.data.spirv_shader_job.spirv_job.optimized = True
    # Derived from.
    # TODO: This could be automated.
    output_metadata.derived_from.append(recipe.spirv_shader_job_artifact)
    if len(recipe.spirv_opt_artifact) > 0:
        output_metadata.derived_from.append(recipe.spirv_opt_artifact)

    # Input shader job json file comes from the input artifact metadata.
    input_shader_job_json = artifact_get_inner_file_path(
        input_spirv_artifact.path,
        input_spirv_artifact.metadata.data.spirv_shader_job.spirv_job.shader_job_file,
    )

    # Output shader job json file is the same, but in the output artifact path.
    output_shader_job_json = artifact_get_inner_file_path(
        output_artifact_path,
        input_spirv_artifact.metadata.data.spirv_shader_job.spirv_job.shader_job_file,
    )

    if len(recipe.spirv_opt_artifact) > 0:
        raise NotImplementedError('Not yet implemented the use of spirv_opt_artifact')

    spirv_opt_file_path = tool_on_path('spirv-opt')

    run_spirv_opt_on_spirv_shader_job(
        input_shader_job_json,
        output_shader_job_json,
        list(recipe.spirv_opt_args),
        spirv_opt_file_path,
    )

    artifact_write_metadata(output_artifact_path, output_metadata)


def recipe_glsl_shader_job_add_red_pixels_run(
    output_artifact_path: str,
    recipe: RecipeGlslShaderJobAddRedPixels,
):
    artifact_execute_recipe_if_needed(recipe.glsl_shader_job_artifact)
    if len(recipe.graphics_fuzz_artifact) > 0:
        artifact_execute_recipe_if_needed(recipe.graphics_fuzz_artifact)

    # Wrap input artifact for convenience.
    input_glsl_artifact = Artifact(recipe.glsl_shader_job_artifact)

    output_metadata = ArtifactMetadata()
    output_metadata.CopyFrom(input_glsl_artifact.metadata)
    output_metadata.data.glsl_shader_job.red_pixel_at_top_left = True
    output_metadata.derived_from.append(recipe.glsl_shader_job_artifact)
    if len(recipe.graphics_fuzz_artifact) > 0:
        output_metadata.derived_from.append(recipe.graphics_fuzz_artifact)

    input_json_path = artifact_get_inner_file_path(
        input_glsl_artifact.path,
        input_glsl_artifact.metadata.data.glsl_shader_job.shader_job_file,
    )

    output_json_path = artifact_get_inner_file_path(
        output_artifact_path,
        output_metadata.data.glsl_shader_job.shader_job_file,
    )

    run_glsl_shader_job_add_red_pixels(
        input_json_path,
        output_json_path,
    )

    artifact_write_metadata(output_artifact_path, output_metadata)


def recipe_spirv_asm_shader_job_to_amber_script_run(
    output_artifact_path: str,
    recipe: RecipeSpirvAsmShaderJobToAmberScript,
):
    artifact_execute_recipe_if_needed(recipe.spirv_asm_shader_job_artifact)

    # Wrap input artifact for convenience.
    input_artifact = Artifact(recipe.spirv_asm_shader_job_artifact)

    input_json_path = artifact_get_inner_file_path(
        input_artifact.path,
        input_artifact.metadata.data.spirv_asm_shader_job.spirv_job.shader_job_file,
    )

    input_glsl_json_path = None
    input_glsl_artifact_path = \
        input_artifact.metadata.data.spirv_asm_shader_job.spirv_job.glsl_shader_job_source_artifact
    if len(input_glsl_artifact_path) > 0:
        input_glsl_artifact = artifact_read_metadata(input_glsl_artifact_path)
        input_glsl_json_path = artifact_get_inner_file_path(
            input_glsl_artifact_path,
            input_glsl_artifact.data.glsl_shader_job.shader_job_file,
        )

    add_red_pixel_probe = False
    if recipe.make_self_contained_test:
        if not input_artifact.metadata.data.spirv_asm_shader_job.spirv_job.red_pixel_at_top_left:
            raise NotImplementedError(
                'Cannot create self-contained AmberScript test unless the input SPIR-V shader job '
                'has "red_pixel_at_top_left: true"'
            )
        add_red_pixel_probe = True

    output_amber_script_file_name = recipe.amber_script_output_file
    if len(output_amber_script_file_name) == 0:
        output_amber_script_file_name = (
            util.remove_end(input_json_path.name, '.json') + '.amber_script'
        )

    output_amber_script_file_path = artifact_get_inner_file_path(
        output_artifact_path,
        output_amber_script_file_name,
    )

    output_metadata = ArtifactMetadata()
    output_metadata.data.amber_script.amber_script_file = output_amber_script_file_name
    if add_red_pixel_probe:
        output_metadata.data.amber_script.self_contained_test = True
    output_metadata.derived_from.append(input_artifact.path)

    glsl_source_artifact = \
        input_artifact.metadata.data.spirv_asm_shader_job.spirv_job.glsl_shader_job_source_artifact
    if len(glsl_source_artifact) > 0:
        output_metadata.derived_from.append(glsl_source_artifact)

    run_spirv_asm_shader_job_to_amber_script(
        input_json_path,
        output_amber_script_file_path,
        add_red_pixel_probe,
        input_glsl_json_path,
    )

    artifact_write_metadata(output_artifact_path, output_metadata)


def recipe_spirv_shader_job_to_spirv_asm_shader_job_run(
    output_artifact_path: str,
    recipe: RecipeSpirvShaderJobToSpirvAsmShaderJob,
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
        input_artifact.path,
        input_artifact.metadata.data.spirv_shader_job.spirv_job.shader_job_file,
    )

    output_json_path = artifact_get_inner_file_path(
        output_artifact_path,
        output_metadata.data.spirv_asm_shader_job.spirv_job.shader_job_file,
    )

    if len(recipe.spirv_dis_artifact) > 0:
        raise NotImplementedError('Not yet implemented the use of spirv_dis_artifact')

    spirv_dis_file_path = tool_on_path('spirv-dis')

    run_spirv_shader_job_to_spirv_asm_shader_job(
        input_json_path,
        output_json_path,
        spirv_dis_file_path,
    )

    artifact_write_metadata(output_artifact_path, output_metadata)


def artifact_create_amber_script_from_glsl_shader_job_artifact(
    work_artifact_path: str,
    input_artifact_path: str,
    spirv_opt_args: Optional[Iterable[str]]
):
    next_input = input_artifact_path

    next_input = artifact_write_recipe(
        work_artifact_path + '/red_pixels',
        Recipe(
            glsl_shader_job_add_red_pixels=RecipeGlslShaderJobAddRedPixels(
                glsl_shader_job_artifact=next_input,
                graphics_fuzz_artifact='',
            ),
        ),
    )

    next_input = artifact_write_recipe(
        work_artifact_path + '/red_pixels_spirv',
        Recipe(
            glsl_shader_job_to_spirv_shader_job=RecipeGlslShaderJobToSpirvShaderJob(
                glsl_shader_job_artifact=next_input,
                glslang_validator_artifact='',
            ),
        ),
    )

    if spirv_opt_args:
        next_input = artifact_write_recipe(
            work_artifact_path + '/red_pixels_spirv_o',
            Recipe(
                spirv_shader_job_to_spirv_shader_job_opt=RecipeSpirvShaderJobToSpirvShaderJobOpt(
                    spirv_shader_job_artifact=next_input,
                    spirv_opt_args=spirv_opt_args,
                    spirv_opt_artifact='',
                ),
            ),
        )

    next_input = artifact_write_recipe(
        work_artifact_path + '/red_pixels_spirv_o_asm',
        Recipe(
            spirv_shader_job_to_spirv_asm_shader_job=RecipeSpirvShaderJobToSpirvAsmShaderJob(
                spirv_shader_job_artifact=next_input,
                spirv_dis_artifact='',
            ),
        ),
    )

    next_input = artifact_write_recipe(
        work_artifact_path + '/red_pixels_spirv_o_asm_amber',
        Recipe(
            spirv_asm_shader_job_to_amber_script=RecipeSpirvAsmShaderJobToAmberScript(
                spirv_asm_shader_job_artifact=next_input,
                make_self_contained_test=True,
                amber_script_output_file='test.amber_script',
            ),
        ),
    )

    artifact_execute_recipe_if_needed(next_input)
