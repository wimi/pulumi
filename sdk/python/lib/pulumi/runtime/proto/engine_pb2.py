# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='engine.proto',
  package='pulumirpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x65ngine.proto\x12\tpulumirpc\x1a\x1bgoogle/protobuf/empty.proto\"x\n\nLogRequest\x12(\n\x08severity\x18\x01 \x01(\x0e\x32\x16.pulumirpc.LogSeverity\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x10\n\x08streamId\x18\x04 \x01(\x05\x12\x10\n\x08isStatus\x18\x05 \x01(\x08*:\n\x0bLogSeverity\x12\t\n\x05\x44\x45\x42UG\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x32@\n\x06\x45ngine\x12\x36\n\x03Log\x12\x15.pulumirpc.LogRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_LOGSEVERITY = _descriptor.EnumDescriptor(
  name='LogSeverity',
  full_name='pulumirpc.LogSeverity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=178,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_LOGSEVERITY)

LogSeverity = enum_type_wrapper.EnumTypeWrapper(_LOGSEVERITY)
DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3



_LOGREQUEST = _descriptor.Descriptor(
  name='LogRequest',
  full_name='pulumirpc.LogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='severity', full_name='pulumirpc.LogRequest.severity', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pulumirpc.LogRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.LogRequest.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamId', full_name='pulumirpc.LogRequest.streamId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isStatus', full_name='pulumirpc.LogRequest.isStatus', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=56,
  serialized_end=176,
)

_LOGREQUEST.fields_by_name['severity'].enum_type = _LOGSEVERITY
DESCRIPTOR.message_types_by_name['LogRequest'] = _LOGREQUEST
DESCRIPTOR.enum_types_by_name['LogSeverity'] = _LOGSEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGREQUEST,
  __module__ = 'engine_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.LogRequest)
  ))
_sym_db.RegisterMessage(LogRequest)



_ENGINE = _descriptor.ServiceDescriptor(
  name='Engine',
  full_name='pulumirpc.Engine',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=238,
  serialized_end=302,
  methods=[
  _descriptor.MethodDescriptor(
    name='Log',
    full_name='pulumirpc.Engine.Log',
    index=0,
    containing_service=None,
    input_type=_LOGREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENGINE)

DESCRIPTOR.services_by_name['Engine'] = _ENGINE

# @@protoc_insertion_point(module_scope)
