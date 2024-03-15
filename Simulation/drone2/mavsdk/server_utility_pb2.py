# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_utility/server_utility.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#server_utility/server_utility.proto\x12\x19mavsdk.rpc.server_utility\x1a\x14mavsdk_options.proto\"^\n\x15SendStatusTextRequest\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).mavsdk.rpc.server_utility.StatusTextType\x12\x0c\n\x04text\x18\x02 \x01(\t\"g\n\x16SendStatusTextResponse\x12M\n\x15server_utility_result\x18\x01 \x01(\x0b\x32..mavsdk.rpc.server_utility.ServerUtilityResult\"\xf3\x01\n\x13ServerUtilityResult\x12\x45\n\x06result\x18\x01 \x01(\x0e\x32\x35.mavsdk.rpc.server_utility.ServerUtilityResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x80\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x04*\xf9\x01\n\x0eStatusTextType\x12\x1a\n\x16STATUS_TEXT_TYPE_DEBUG\x10\x00\x12\x19\n\x15STATUS_TEXT_TYPE_INFO\x10\x01\x12\x1b\n\x17STATUS_TEXT_TYPE_NOTICE\x10\x02\x12\x1c\n\x18STATUS_TEXT_TYPE_WARNING\x10\x03\x12\x1a\n\x16STATUS_TEXT_TYPE_ERROR\x10\x04\x12\x1d\n\x19STATUS_TEXT_TYPE_CRITICAL\x10\x05\x12\x1a\n\x16STATUS_TEXT_TYPE_ALERT\x10\x06\x12\x1e\n\x1aSTATUS_TEXT_TYPE_EMERGENCY\x10\x07\x32\x93\x01\n\x14ServerUtilityService\x12{\n\x0eSendStatusText\x12\x30.mavsdk.rpc.server_utility.SendStatusTextRequest\x1a\x31.mavsdk.rpc.server_utility.SendStatusTextResponse\"\x04\x80\xb5\x18\x01\x42.\n\x18io.mavsdk.server_utilityB\x12ServerUtilityProtob\x06proto3')

_STATUSTEXTTYPE = DESCRIPTOR.enum_types_by_name['StatusTextType']
StatusTextType = enum_type_wrapper.EnumTypeWrapper(_STATUSTEXTTYPE)
STATUS_TEXT_TYPE_DEBUG = 0
STATUS_TEXT_TYPE_INFO = 1
STATUS_TEXT_TYPE_NOTICE = 2
STATUS_TEXT_TYPE_WARNING = 3
STATUS_TEXT_TYPE_ERROR = 4
STATUS_TEXT_TYPE_CRITICAL = 5
STATUS_TEXT_TYPE_ALERT = 6
STATUS_TEXT_TYPE_EMERGENCY = 7


_SENDSTATUSTEXTREQUEST = DESCRIPTOR.message_types_by_name['SendStatusTextRequest']
_SENDSTATUSTEXTRESPONSE = DESCRIPTOR.message_types_by_name['SendStatusTextResponse']
_SERVERUTILITYRESULT = DESCRIPTOR.message_types_by_name['ServerUtilityResult']
_SERVERUTILITYRESULT_RESULT = _SERVERUTILITYRESULT.enum_types_by_name['Result']
SendStatusTextRequest = _reflection.GeneratedProtocolMessageType('SendStatusTextRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTATUSTEXTREQUEST,
  '__module__' : 'server_utility.server_utility_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.server_utility.SendStatusTextRequest)
  })
_sym_db.RegisterMessage(SendStatusTextRequest)

SendStatusTextResponse = _reflection.GeneratedProtocolMessageType('SendStatusTextResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTATUSTEXTRESPONSE,
  '__module__' : 'server_utility.server_utility_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.server_utility.SendStatusTextResponse)
  })
_sym_db.RegisterMessage(SendStatusTextResponse)

ServerUtilityResult = _reflection.GeneratedProtocolMessageType('ServerUtilityResult', (_message.Message,), {
  'DESCRIPTOR' : _SERVERUTILITYRESULT,
  '__module__' : 'server_utility.server_utility_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.server_utility.ServerUtilityResult)
  })
_sym_db.RegisterMessage(ServerUtilityResult)

_SERVERUTILITYSERVICE = DESCRIPTOR.services_by_name['ServerUtilityService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030io.mavsdk.server_utilityB\022ServerUtilityProto'
  _SERVERUTILITYSERVICE.methods_by_name['SendStatusText']._options = None
  _SERVERUTILITYSERVICE.methods_by_name['SendStatusText']._serialized_options = b'\200\265\030\001'
  _STATUSTEXTTYPE._serialized_start=536
  _STATUSTEXTTYPE._serialized_end=785
  _SENDSTATUSTEXTREQUEST._serialized_start=88
  _SENDSTATUSTEXTREQUEST._serialized_end=182
  _SENDSTATUSTEXTRESPONSE._serialized_start=184
  _SENDSTATUSTEXTRESPONSE._serialized_end=287
  _SERVERUTILITYRESULT._serialized_start=290
  _SERVERUTILITYRESULT._serialized_end=533
  _SERVERUTILITYRESULT_RESULT._serialized_start=405
  _SERVERUTILITYRESULT_RESULT._serialized_end=533
  _SERVERUTILITYSERVICE._serialized_start=788
  _SERVERUTILITYSERVICE._serialized_end=935
# @@protoc_insertion_point(module_scope)