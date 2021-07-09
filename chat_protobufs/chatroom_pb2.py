# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatroom.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chatroom.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63hatroom.proto\"\x1a\n\x07Nothing\x12\x0f\n\x07nothing\x18\x01 \x01(\x08\";\n\x12sendMessageRequest\x12\x13\n\x0bsentMessage\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\"%\n\x11\x63onnectionRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\"&\n\x11\x63onnectionConfirm\x12\x11\n\tconnected\x18\x01 \x01(\x08\"\"\n\x0eonCloseRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\",\n\x14\x64isconnectionConfirm\x12\x14\n\x0c\x64isconnected\x18\x01 \x01(\x08\x32\xda\x01\n\x04\x43hat\x12\x30\n\rmessageStream\x12\x08.Nothing\x1a\x13.sendMessageRequest0\x01\x12,\n\x0bsendMessage\x12\x13.sendMessageRequest\x1a\x08.Nothing\x12\x37\n\rconnectedUser\x12\x12.connectionRequest\x1a\x12.connectionConfirm\x12\x39\n\x0fonDisconnection\x12\x0f.onCloseRequest\x1a\x15.disconnectionConfirmb\x06proto3'
)




_NOTHING = _descriptor.Descriptor(
  name='Nothing',
  full_name='Nothing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nothing', full_name='Nothing.nothing', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=18,
  serialized_end=44,
)


_SENDMESSAGEREQUEST = _descriptor.Descriptor(
  name='sendMessageRequest',
  full_name='sendMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentMessage', full_name='sendMessageRequest.sentMessage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userName', full_name='sendMessageRequest.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=46,
  serialized_end=105,
)


_CONNECTIONREQUEST = _descriptor.Descriptor(
  name='connectionRequest',
  full_name='connectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='connectionRequest.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=107,
  serialized_end=144,
)


_CONNECTIONCONFIRM = _descriptor.Descriptor(
  name='connectionConfirm',
  full_name='connectionConfirm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='connectionConfirm.connected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=146,
  serialized_end=184,
)


_ONCLOSEREQUEST = _descriptor.Descriptor(
  name='onCloseRequest',
  full_name='onCloseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='onCloseRequest.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=186,
  serialized_end=220,
)


_DISCONNECTIONCONFIRM = _descriptor.Descriptor(
  name='disconnectionConfirm',
  full_name='disconnectionConfirm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='disconnected', full_name='disconnectionConfirm.disconnected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=222,
  serialized_end=266,
)

DESCRIPTOR.message_types_by_name['Nothing'] = _NOTHING
DESCRIPTOR.message_types_by_name['sendMessageRequest'] = _SENDMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['connectionRequest'] = _CONNECTIONREQUEST
DESCRIPTOR.message_types_by_name['connectionConfirm'] = _CONNECTIONCONFIRM
DESCRIPTOR.message_types_by_name['onCloseRequest'] = _ONCLOSEREQUEST
DESCRIPTOR.message_types_by_name['disconnectionConfirm'] = _DISCONNECTIONCONFIRM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Nothing = _reflection.GeneratedProtocolMessageType('Nothing', (_message.Message,), {
  'DESCRIPTOR' : _NOTHING,
  '__module__' : 'chatroom_pb2'
  # @@protoc_insertion_point(class_scope:Nothing)
  })
_sym_db.RegisterMessage(Nothing)

sendMessageRequest = _reflection.GeneratedProtocolMessageType('sendMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGEREQUEST,
  '__module__' : 'chatroom_pb2'
  # @@protoc_insertion_point(class_scope:sendMessageRequest)
  })
_sym_db.RegisterMessage(sendMessageRequest)

connectionRequest = _reflection.GeneratedProtocolMessageType('connectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONREQUEST,
  '__module__' : 'chatroom_pb2'
  # @@protoc_insertion_point(class_scope:connectionRequest)
  })
_sym_db.RegisterMessage(connectionRequest)

connectionConfirm = _reflection.GeneratedProtocolMessageType('connectionConfirm', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONCONFIRM,
  '__module__' : 'chatroom_pb2'
  # @@protoc_insertion_point(class_scope:connectionConfirm)
  })
_sym_db.RegisterMessage(connectionConfirm)

onCloseRequest = _reflection.GeneratedProtocolMessageType('onCloseRequest', (_message.Message,), {
  'DESCRIPTOR' : _ONCLOSEREQUEST,
  '__module__' : 'chatroom_pb2'
  # @@protoc_insertion_point(class_scope:onCloseRequest)
  })
_sym_db.RegisterMessage(onCloseRequest)

disconnectionConfirm = _reflection.GeneratedProtocolMessageType('disconnectionConfirm', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTIONCONFIRM,
  '__module__' : 'chatroom_pb2'
  # @@protoc_insertion_point(class_scope:disconnectionConfirm)
  })
_sym_db.RegisterMessage(disconnectionConfirm)



_CHAT = _descriptor.ServiceDescriptor(
  name='Chat',
  full_name='Chat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=269,
  serialized_end=487,
  methods=[
  _descriptor.MethodDescriptor(
    name='messageStream',
    full_name='Chat.messageStream',
    index=0,
    containing_service=None,
    input_type=_NOTHING,
    output_type=_SENDMESSAGEREQUEST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendMessage',
    full_name='Chat.sendMessage',
    index=1,
    containing_service=None,
    input_type=_SENDMESSAGEREQUEST,
    output_type=_NOTHING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='connectedUser',
    full_name='Chat.connectedUser',
    index=2,
    containing_service=None,
    input_type=_CONNECTIONREQUEST,
    output_type=_CONNECTIONCONFIRM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='onDisconnection',
    full_name='Chat.onDisconnection',
    index=3,
    containing_service=None,
    input_type=_ONCLOSEREQUEST,
    output_type=_DISCONNECTIONCONFIRM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAT)

DESCRIPTOR.services_by_name['Chat'] = _CHAT

# @@protoc_insertion_point(module_scope)
