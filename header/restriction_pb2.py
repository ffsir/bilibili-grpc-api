# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: restriction.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='restriction.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11restriction.proto\"\x9a\x01\n\x0bRestriction\x12\x15\n\rteenagersMode\x18\x01 \x01(\x08\x12\x13\n\x0blessonsMode\x18\x02 \x01(\x08\x12\x1f\n\x04mode\x18\x03 \x01(\x0e\x32\x11.Restriction.Mode\x12\x0e\n\x06review\x18\x04 \x01(\x08\".\n\x04Mode\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tTEENAGERS\x10\x01\x12\x0b\n\x07LESSONS\x10\x02'
)



_RESTRICTION_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='Restriction.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEENAGERS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESSONS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=130,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_RESTRICTION_MODE)


_RESTRICTION = _descriptor.Descriptor(
  name='Restriction',
  full_name='Restriction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='teenagersMode', full_name='Restriction.teenagersMode', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lessonsMode', full_name='Restriction.lessonsMode', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='Restriction.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='review', full_name='Restriction.review', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESTRICTION_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=176,
)

_RESTRICTION.fields_by_name['mode'].enum_type = _RESTRICTION_MODE
_RESTRICTION_MODE.containing_type = _RESTRICTION
DESCRIPTOR.message_types_by_name['Restriction'] = _RESTRICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Restriction = _reflection.GeneratedProtocolMessageType('Restriction', (_message.Message,), {
  'DESCRIPTOR' : _RESTRICTION,
  '__module__' : 'restriction_pb2'
  # @@protoc_insertion_point(class_scope:Restriction)
  })
_sym_db.RegisterMessage(Restriction)


# @@protoc_insertion_point(module_scope)
