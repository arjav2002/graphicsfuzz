# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recipe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import artifact_pb2 as artifact__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='recipe.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0crecipe.proto\x1a\x0c\x63ommon.proto\x1a\x0e\x61rtifact.proto\"\xe9\x03\n\x06Recipe\x12!\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x0e.RecipeCommandH\x00\x12S\n#glsl_shader_job_to_spirv_shader_job\x18\x02 \x01(\x0b\x32$.RecipeGlslShaderJobToSpirvShaderJobH\x00\x12\\\n(spirv_shader_job_to_spirv_shader_job_opt\x18\x03 \x01(\x0b\x32(.RecipeSpirvShaderJobToSpirvShaderJobOptH\x00\x12J\n\x1eglsl_shader_job_add_red_pixels\x18\x04 \x01(\x0b\x32 .RecipeGlslShaderJobAddRedPixelsH\x00\x12U\n$spirv_asm_shader_job_to_amber_script\x18\x05 \x01(\x0b\x32%.RecipeSpirvAsmShaderJobToAmberScriptH\x00\x12\\\n(spirv_shader_job_to_spirv_asm_shader_job\x18\x06 \x01(\x0b\x32(.RecipeSpirvShaderJobToSpirvAsmShaderJobH\x00\x42\x08\n\x06recipe\" \n\rRecipeCommand\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\"k\n#RecipeGlslShaderJobToSpirvShaderJob\x12 \n\x18glsl_shader_job_artifact\x18\x01 \x01(\t\x12\"\n\x1aglslang_validator_artifact\x18\x02 \x01(\t\"\x80\x01\n\'RecipeSpirvShaderJobToSpirvShaderJobOpt\x12!\n\x19spirv_shader_job_artifact\x18\x01 \x01(\t\x12\x16\n\x0espirv_opt_args\x18\x02 \x03(\t\x12\x1a\n\x12spirv_opt_artifact\x18\x03 \x01(\t\"c\n\x1fRecipeGlslShaderJobAddRedPixels\x12 \n\x18glsl_shader_job_artifact\x18\x01 \x01(\t\x12\x1e\n\x16graphics_fuzz_artifact\x18\x02 \x01(\t\"h\n\'RecipeSpirvShaderJobToSpirvAsmShaderJob\x12!\n\x19spirv_shader_job_artifact\x18\x01 \x01(\t\x12\x1a\n\x12spirv_dis_artifact\x18\x02 \x01(\t\"\xe1\x02\n$RecipeSpirvAsmShaderJobToAmberScript\x12%\n\x1dspirv_asm_shader_job_artifact\x18\x01 \x01(\t\x12 \n\x18make_self_contained_test\x18\x02 \x01(\x08\x12 \n\x18\x61mber_script_output_file\x18\x03 \x01(\t\x12&\n\x1e\x63opyright_header_text_artifact\x18\x04 \x01(\t\x12\x1d\n\x15\x61\x64\x64_generated_comment\x18\x05 \x01(\x08\x12!\n\x19\x61\x64\x64_graphics_fuzz_comment\x18\x06 \x01(\x08\x12\x1d\n\x15\x63omment_text_artifact\x18\x07 \x01(\t\x12\"\n\x1a\x61\x64\x64_glsl_source_as_comment\x18\x08 \x01(\x08\x12!\n\x19use_default_fence_timeout\x18\t \x01(\x08\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,artifact__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RECIPE = _descriptor.Descriptor(
  name='Recipe',
  full_name='Recipe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='Recipe.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='glsl_shader_job_to_spirv_shader_job', full_name='Recipe.glsl_shader_job_to_spirv_shader_job', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spirv_shader_job_to_spirv_shader_job_opt', full_name='Recipe.spirv_shader_job_to_spirv_shader_job_opt', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='glsl_shader_job_add_red_pixels', full_name='Recipe.glsl_shader_job_add_red_pixels', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spirv_asm_shader_job_to_amber_script', full_name='Recipe.spirv_asm_shader_job_to_amber_script', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spirv_shader_job_to_spirv_asm_shader_job', full_name='Recipe.spirv_shader_job_to_spirv_asm_shader_job', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='recipe', full_name='Recipe.recipe',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=47,
  serialized_end=536,
)


_RECIPECOMMAND = _descriptor.Descriptor(
  name='RecipeCommand',
  full_name='RecipeCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='RecipeCommand.command', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=570,
)


_RECIPEGLSLSHADERJOBTOSPIRVSHADERJOB = _descriptor.Descriptor(
  name='RecipeGlslShaderJobToSpirvShaderJob',
  full_name='RecipeGlslShaderJobToSpirvShaderJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='glsl_shader_job_artifact', full_name='RecipeGlslShaderJobToSpirvShaderJob.glsl_shader_job_artifact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='glslang_validator_artifact', full_name='RecipeGlslShaderJobToSpirvShaderJob.glslang_validator_artifact', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=679,
)


_RECIPESPIRVSHADERJOBTOSPIRVSHADERJOBOPT = _descriptor.Descriptor(
  name='RecipeSpirvShaderJobToSpirvShaderJobOpt',
  full_name='RecipeSpirvShaderJobToSpirvShaderJobOpt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spirv_shader_job_artifact', full_name='RecipeSpirvShaderJobToSpirvShaderJobOpt.spirv_shader_job_artifact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spirv_opt_args', full_name='RecipeSpirvShaderJobToSpirvShaderJobOpt.spirv_opt_args', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spirv_opt_artifact', full_name='RecipeSpirvShaderJobToSpirvShaderJobOpt.spirv_opt_artifact', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=810,
)


_RECIPEGLSLSHADERJOBADDREDPIXELS = _descriptor.Descriptor(
  name='RecipeGlslShaderJobAddRedPixels',
  full_name='RecipeGlslShaderJobAddRedPixels',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='glsl_shader_job_artifact', full_name='RecipeGlslShaderJobAddRedPixels.glsl_shader_job_artifact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graphics_fuzz_artifact', full_name='RecipeGlslShaderJobAddRedPixels.graphics_fuzz_artifact', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=812,
  serialized_end=911,
)


_RECIPESPIRVSHADERJOBTOSPIRVASMSHADERJOB = _descriptor.Descriptor(
  name='RecipeSpirvShaderJobToSpirvAsmShaderJob',
  full_name='RecipeSpirvShaderJobToSpirvAsmShaderJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spirv_shader_job_artifact', full_name='RecipeSpirvShaderJobToSpirvAsmShaderJob.spirv_shader_job_artifact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spirv_dis_artifact', full_name='RecipeSpirvShaderJobToSpirvAsmShaderJob.spirv_dis_artifact', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=913,
  serialized_end=1017,
)


_RECIPESPIRVASMSHADERJOBTOAMBERSCRIPT = _descriptor.Descriptor(
  name='RecipeSpirvAsmShaderJobToAmberScript',
  full_name='RecipeSpirvAsmShaderJobToAmberScript',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spirv_asm_shader_job_artifact', full_name='RecipeSpirvAsmShaderJobToAmberScript.spirv_asm_shader_job_artifact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='make_self_contained_test', full_name='RecipeSpirvAsmShaderJobToAmberScript.make_self_contained_test', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amber_script_output_file', full_name='RecipeSpirvAsmShaderJobToAmberScript.amber_script_output_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='copyright_header_text_artifact', full_name='RecipeSpirvAsmShaderJobToAmberScript.copyright_header_text_artifact', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_generated_comment', full_name='RecipeSpirvAsmShaderJobToAmberScript.add_generated_comment', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_graphics_fuzz_comment', full_name='RecipeSpirvAsmShaderJobToAmberScript.add_graphics_fuzz_comment', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment_text_artifact', full_name='RecipeSpirvAsmShaderJobToAmberScript.comment_text_artifact', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_glsl_source_as_comment', full_name='RecipeSpirvAsmShaderJobToAmberScript.add_glsl_source_as_comment', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_default_fence_timeout', full_name='RecipeSpirvAsmShaderJobToAmberScript.use_default_fence_timeout', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1020,
  serialized_end=1373,
)

_RECIPE.fields_by_name['command'].message_type = _RECIPECOMMAND
_RECIPE.fields_by_name['glsl_shader_job_to_spirv_shader_job'].message_type = _RECIPEGLSLSHADERJOBTOSPIRVSHADERJOB
_RECIPE.fields_by_name['spirv_shader_job_to_spirv_shader_job_opt'].message_type = _RECIPESPIRVSHADERJOBTOSPIRVSHADERJOBOPT
_RECIPE.fields_by_name['glsl_shader_job_add_red_pixels'].message_type = _RECIPEGLSLSHADERJOBADDREDPIXELS
_RECIPE.fields_by_name['spirv_asm_shader_job_to_amber_script'].message_type = _RECIPESPIRVASMSHADERJOBTOAMBERSCRIPT
_RECIPE.fields_by_name['spirv_shader_job_to_spirv_asm_shader_job'].message_type = _RECIPESPIRVSHADERJOBTOSPIRVASMSHADERJOB
_RECIPE.oneofs_by_name['recipe'].fields.append(
  _RECIPE.fields_by_name['command'])
_RECIPE.fields_by_name['command'].containing_oneof = _RECIPE.oneofs_by_name['recipe']
_RECIPE.oneofs_by_name['recipe'].fields.append(
  _RECIPE.fields_by_name['glsl_shader_job_to_spirv_shader_job'])
_RECIPE.fields_by_name['glsl_shader_job_to_spirv_shader_job'].containing_oneof = _RECIPE.oneofs_by_name['recipe']
_RECIPE.oneofs_by_name['recipe'].fields.append(
  _RECIPE.fields_by_name['spirv_shader_job_to_spirv_shader_job_opt'])
_RECIPE.fields_by_name['spirv_shader_job_to_spirv_shader_job_opt'].containing_oneof = _RECIPE.oneofs_by_name['recipe']
_RECIPE.oneofs_by_name['recipe'].fields.append(
  _RECIPE.fields_by_name['glsl_shader_job_add_red_pixels'])
_RECIPE.fields_by_name['glsl_shader_job_add_red_pixels'].containing_oneof = _RECIPE.oneofs_by_name['recipe']
_RECIPE.oneofs_by_name['recipe'].fields.append(
  _RECIPE.fields_by_name['spirv_asm_shader_job_to_amber_script'])
_RECIPE.fields_by_name['spirv_asm_shader_job_to_amber_script'].containing_oneof = _RECIPE.oneofs_by_name['recipe']
_RECIPE.oneofs_by_name['recipe'].fields.append(
  _RECIPE.fields_by_name['spirv_shader_job_to_spirv_asm_shader_job'])
_RECIPE.fields_by_name['spirv_shader_job_to_spirv_asm_shader_job'].containing_oneof = _RECIPE.oneofs_by_name['recipe']
DESCRIPTOR.message_types_by_name['Recipe'] = _RECIPE
DESCRIPTOR.message_types_by_name['RecipeCommand'] = _RECIPECOMMAND
DESCRIPTOR.message_types_by_name['RecipeGlslShaderJobToSpirvShaderJob'] = _RECIPEGLSLSHADERJOBTOSPIRVSHADERJOB
DESCRIPTOR.message_types_by_name['RecipeSpirvShaderJobToSpirvShaderJobOpt'] = _RECIPESPIRVSHADERJOBTOSPIRVSHADERJOBOPT
DESCRIPTOR.message_types_by_name['RecipeGlslShaderJobAddRedPixels'] = _RECIPEGLSLSHADERJOBADDREDPIXELS
DESCRIPTOR.message_types_by_name['RecipeSpirvShaderJobToSpirvAsmShaderJob'] = _RECIPESPIRVSHADERJOBTOSPIRVASMSHADERJOB
DESCRIPTOR.message_types_by_name['RecipeSpirvAsmShaderJobToAmberScript'] = _RECIPESPIRVASMSHADERJOBTOAMBERSCRIPT

Recipe = _reflection.GeneratedProtocolMessageType('Recipe', (_message.Message,), dict(
  DESCRIPTOR = _RECIPE,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:Recipe)
  ))
_sym_db.RegisterMessage(Recipe)

RecipeCommand = _reflection.GeneratedProtocolMessageType('RecipeCommand', (_message.Message,), dict(
  DESCRIPTOR = _RECIPECOMMAND,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:RecipeCommand)
  ))
_sym_db.RegisterMessage(RecipeCommand)

RecipeGlslShaderJobToSpirvShaderJob = _reflection.GeneratedProtocolMessageType('RecipeGlslShaderJobToSpirvShaderJob', (_message.Message,), dict(
  DESCRIPTOR = _RECIPEGLSLSHADERJOBTOSPIRVSHADERJOB,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:RecipeGlslShaderJobToSpirvShaderJob)
  ))
_sym_db.RegisterMessage(RecipeGlslShaderJobToSpirvShaderJob)

RecipeSpirvShaderJobToSpirvShaderJobOpt = _reflection.GeneratedProtocolMessageType('RecipeSpirvShaderJobToSpirvShaderJobOpt', (_message.Message,), dict(
  DESCRIPTOR = _RECIPESPIRVSHADERJOBTOSPIRVSHADERJOBOPT,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:RecipeSpirvShaderJobToSpirvShaderJobOpt)
  ))
_sym_db.RegisterMessage(RecipeSpirvShaderJobToSpirvShaderJobOpt)

RecipeGlslShaderJobAddRedPixels = _reflection.GeneratedProtocolMessageType('RecipeGlslShaderJobAddRedPixels', (_message.Message,), dict(
  DESCRIPTOR = _RECIPEGLSLSHADERJOBADDREDPIXELS,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:RecipeGlslShaderJobAddRedPixels)
  ))
_sym_db.RegisterMessage(RecipeGlslShaderJobAddRedPixels)

RecipeSpirvShaderJobToSpirvAsmShaderJob = _reflection.GeneratedProtocolMessageType('RecipeSpirvShaderJobToSpirvAsmShaderJob', (_message.Message,), dict(
  DESCRIPTOR = _RECIPESPIRVSHADERJOBTOSPIRVASMSHADERJOB,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:RecipeSpirvShaderJobToSpirvAsmShaderJob)
  ))
_sym_db.RegisterMessage(RecipeSpirvShaderJobToSpirvAsmShaderJob)

RecipeSpirvAsmShaderJobToAmberScript = _reflection.GeneratedProtocolMessageType('RecipeSpirvAsmShaderJobToAmberScript', (_message.Message,), dict(
  DESCRIPTOR = _RECIPESPIRVASMSHADERJOBTOAMBERSCRIPT,
  __module__ = 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:RecipeSpirvAsmShaderJobToAmberScript)
  ))
_sym_db.RegisterMessage(RecipeSpirvAsmShaderJobToAmberScript)


# @@protoc_insertion_point(module_scope)