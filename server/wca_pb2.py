# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wca.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wca.proto',
  package='wca',
  syntax='proto3',
  serialized_options=_b('\n\016edu.cmu.cs.wcaB\006Protos'),
  serialized_pb=_b('\n\twca.proto\x12\x03wca\"\x95\x01\n\x0eToServerExtras\x12\x0c\n\x04step\x18\x01 \x01(\t\x12\x31\n\nclient_cmd\x18\x02 \x01(\x0e\x32\x1d.wca.ToServerExtras.ClientCmd\"B\n\tClientCmd\x12\n\n\x06NO_CMD\x10\x00\x12\x0e\n\nZOOM_START\x10\x01\x12\r\n\tZOOM_STOP\x10\x02\x12\n\n\x06REPORT\x10\x03\"\xa1\x02\n\x0eToClientExtras\x12\x0c\n\x04step\x18\x01 \x01(\t\x12 \n\tzoom_info\x18\x02 \x01(\x0b\x32\r.wca.ZoomInfo\x12\x33\n\x0bzoom_result\x18\x03 \x01(\x0e\x32\x1e.wca.ToClientExtras.ZoomResult\x12\x31\n\nuser_ready\x18\x04 \x01(\x0e\x32\x1d.wca.ToClientExtras.UserReady\":\n\nZoomResult\x12\x0b\n\x07NO_CALL\x10\x00\x12\x0e\n\nCALL_START\x10\x01\x12\x0f\n\x0b\x45XPERT_BUSY\x10\x02\";\n\tUserReady\x12\r\n\tNO_CHANGE\x10\x00\x12\x07\n\x03SET\x10\x01\x12\t\n\x05\x43LEAR\x10\x02\x12\x0b\n\x07\x44ISABLE\x10\x03\"O\n\x08ZoomInfo\x12\x11\n\tjwt_token\x18\x01 \x01(\t\x12\x16\n\x0emeeting_number\x18\x02 \x01(\t\x12\x18\n\x10meeting_password\x18\x03 \x01(\tB\x18\n\x0e\x65\x64u.cmu.cs.wcaB\x06Protosb\x06proto3')
)



_TOSERVEREXTRAS_CLIENTCMD = _descriptor.EnumDescriptor(
  name='ClientCmd',
  full_name='wca.ToServerExtras.ClientCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CMD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZOOM_START', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZOOM_STOP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPORT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=102,
  serialized_end=168,
)
_sym_db.RegisterEnumDescriptor(_TOSERVEREXTRAS_CLIENTCMD)

_TOCLIENTEXTRAS_ZOOMRESULT = _descriptor.EnumDescriptor(
  name='ZoomResult',
  full_name='wca.ToClientExtras.ZoomResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_START', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPERT_BUSY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=341,
  serialized_end=399,
)
_sym_db.RegisterEnumDescriptor(_TOCLIENTEXTRAS_ZOOMRESULT)

_TOCLIENTEXTRAS_USERREADY = _descriptor.EnumDescriptor(
  name='UserReady',
  full_name='wca.ToClientExtras.UserReady',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_CHANGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=401,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_TOCLIENTEXTRAS_USERREADY)


_TOSERVEREXTRAS = _descriptor.Descriptor(
  name='ToServerExtras',
  full_name='wca.ToServerExtras',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='wca.ToServerExtras.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_cmd', full_name='wca.ToServerExtras.client_cmd', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOSERVEREXTRAS_CLIENTCMD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=168,
)


_TOCLIENTEXTRAS = _descriptor.Descriptor(
  name='ToClientExtras',
  full_name='wca.ToClientExtras',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='wca.ToClientExtras.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoom_info', full_name='wca.ToClientExtras.zoom_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoom_result', full_name='wca.ToClientExtras.zoom_result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_ready', full_name='wca.ToClientExtras.user_ready', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOCLIENTEXTRAS_ZOOMRESULT,
    _TOCLIENTEXTRAS_USERREADY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=460,
)


_ZOOMINFO = _descriptor.Descriptor(
  name='ZoomInfo',
  full_name='wca.ZoomInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt_token', full_name='wca.ZoomInfo.jwt_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meeting_number', full_name='wca.ZoomInfo.meeting_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meeting_password', full_name='wca.ZoomInfo.meeting_password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=462,
  serialized_end=541,
)

_TOSERVEREXTRAS.fields_by_name['client_cmd'].enum_type = _TOSERVEREXTRAS_CLIENTCMD
_TOSERVEREXTRAS_CLIENTCMD.containing_type = _TOSERVEREXTRAS
_TOCLIENTEXTRAS.fields_by_name['zoom_info'].message_type = _ZOOMINFO
_TOCLIENTEXTRAS.fields_by_name['zoom_result'].enum_type = _TOCLIENTEXTRAS_ZOOMRESULT
_TOCLIENTEXTRAS.fields_by_name['user_ready'].enum_type = _TOCLIENTEXTRAS_USERREADY
_TOCLIENTEXTRAS_ZOOMRESULT.containing_type = _TOCLIENTEXTRAS
_TOCLIENTEXTRAS_USERREADY.containing_type = _TOCLIENTEXTRAS
DESCRIPTOR.message_types_by_name['ToServerExtras'] = _TOSERVEREXTRAS
DESCRIPTOR.message_types_by_name['ToClientExtras'] = _TOCLIENTEXTRAS
DESCRIPTOR.message_types_by_name['ZoomInfo'] = _ZOOMINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToServerExtras = _reflection.GeneratedProtocolMessageType('ToServerExtras', (_message.Message,), {
  'DESCRIPTOR' : _TOSERVEREXTRAS,
  '__module__' : 'wca_pb2'
  # @@protoc_insertion_point(class_scope:wca.ToServerExtras)
  })
_sym_db.RegisterMessage(ToServerExtras)

ToClientExtras = _reflection.GeneratedProtocolMessageType('ToClientExtras', (_message.Message,), {
  'DESCRIPTOR' : _TOCLIENTEXTRAS,
  '__module__' : 'wca_pb2'
  # @@protoc_insertion_point(class_scope:wca.ToClientExtras)
  })
_sym_db.RegisterMessage(ToClientExtras)

ZoomInfo = _reflection.GeneratedProtocolMessageType('ZoomInfo', (_message.Message,), {
  'DESCRIPTOR' : _ZOOMINFO,
  '__module__' : 'wca_pb2'
  # @@protoc_insertion_point(class_scope:wca.ZoomInfo)
  })
_sym_db.RegisterMessage(ZoomInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
