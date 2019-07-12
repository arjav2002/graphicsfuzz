# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gfauto/test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gfauto import common_pb2 as gfauto_dot_common__pb2
from gfauto import device_pb2 as gfauto_dot_device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gfauto/test.proto',
  package='gfauto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11gfauto/test.proto\x12\x06gfauto\x1a\x13gfauto/common.proto\x1a\x13gfauto/device.proto\"\x8b\x01\n\x04Test\x12 \n\x04glsl\x18\x01 \x01(\x0b\x32\x10.gfauto.TestGlslH\x00\x12\x17\n\x0f\x63rash_signature\x18\x02 \x01(\t\x12\x1e\n\x06\x64\x65vice\x18\x03 \x01(\x0b\x32\x0e.gfauto.Device\x12 \n\x08\x62inaries\x18\x04 \x03(\x0b\x32\x0e.gfauto.BinaryB\x06\n\x04test\"\"\n\x08TestGlsl\x12\x16\n\x0espirv_opt_args\x18\x01 \x03(\tb\x06proto3')
  ,
  dependencies=[gfauto_dot_common__pb2.DESCRIPTOR,gfauto_dot_device__pb2.DESCRIPTOR,])




_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='gfauto.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='glsl', full_name='gfauto.Test.glsl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crash_signature', full_name='gfauto.Test.crash_signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='gfauto.Test.device', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaries', full_name='gfauto.Test.binaries', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='test', full_name='gfauto.Test.test',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=211,
)


_TESTGLSL = _descriptor.Descriptor(
  name='TestGlsl',
  full_name='gfauto.TestGlsl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spirv_opt_args', full_name='gfauto.TestGlsl.spirv_opt_args', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=247,
)

_TEST.fields_by_name['glsl'].message_type = _TESTGLSL
_TEST.fields_by_name['device'].message_type = gfauto_dot_device__pb2._DEVICE
_TEST.fields_by_name['binaries'].message_type = gfauto_dot_common__pb2._BINARY
_TEST.oneofs_by_name['test'].fields.append(
  _TEST.fields_by_name['glsl'])
_TEST.fields_by_name['glsl'].containing_oneof = _TEST.oneofs_by_name['test']
DESCRIPTOR.message_types_by_name['Test'] = _TEST
DESCRIPTOR.message_types_by_name['TestGlsl'] = _TESTGLSL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Test = _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {
  'DESCRIPTOR' : _TEST,
  '__module__' : 'gfauto.test_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.Test)
  })
_sym_db.RegisterMessage(Test)

TestGlsl = _reflection.GeneratedProtocolMessageType('TestGlsl', (_message.Message,), {
  'DESCRIPTOR' : _TESTGLSL,
  '__module__' : 'gfauto.test_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.TestGlsl)
  })
_sym_db.RegisterMessage(TestGlsl)


# @@protoc_insertion_point(module_scope)