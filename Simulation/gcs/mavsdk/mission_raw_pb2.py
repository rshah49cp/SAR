# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mission_raw/mission_raw.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmission_raw/mission_raw.proto\x12\x16mavsdk.rpc.mission_raw\x1a\x14mavsdk_options.proto\"R\n\x14UploadMissionRequest\x12:\n\rmission_items\x18\x01 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\"]\n\x15UploadMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"S\n\x15UploadGeofenceRequest\x12:\n\rmission_items\x18\x01 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\"^\n\x16UploadGeofenceResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"V\n\x18UploadRallyPointsRequest\x12:\n\rmission_items\x18\x01 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\"a\n\x19UploadRallyPointsResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"\x1c\n\x1a\x43\x61ncelMissionUploadRequest\"c\n\x1b\x43\x61ncelMissionUploadResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"\x18\n\x16\x44ownloadMissionRequest\"\x9b\x01\n\x17\x44ownloadMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\x12:\n\rmission_items\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\"\x1e\n\x1c\x43\x61ncelMissionDownloadRequest\"e\n\x1d\x43\x61ncelMissionDownloadResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"\x15\n\x13StartMissionRequest\"\\\n\x14StartMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"\x15\n\x13PauseMissionRequest\"\\\n\x14PauseMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"\x15\n\x13\x43learMissionRequest\"\\\n\x14\x43learMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"-\n\x1cSetCurrentMissionItemRequest\x12\r\n\x05index\x18\x01 \x01(\x05\"e\n\x1dSetCurrentMissionItemResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\"!\n\x1fSubscribeMissionProgressRequest\"\\\n\x17MissionProgressResponse\x12\x41\n\x10mission_progress\x18\x01 \x01(\x0b\x32\'.mavsdk.rpc.mission_raw.MissionProgress\" \n\x1eSubscribeMissionChangedRequest\"1\n\x16MissionChangedResponse\x12\x17\n\x0fmission_changed\x18\x01 \x01(\x08\";\n\"ImportQgroundcontrolMissionRequest\x12\x15\n\rqgc_plan_path\x18\x01 \x01(\t\"\xb3\x01\n#ImportQgroundcontrolMissionResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\x12\x46\n\x13mission_import_data\x18\x02 \x01(\x0b\x32).mavsdk.rpc.mission_raw.MissionImportData\"@\n,ImportQgroundcontrolMissionFromStringRequest\x12\x10\n\x08qgc_plan\x18\x01 \x01(\t\"\xbd\x01\n-ImportQgroundcontrolMissionFromStringResponse\x12\x44\n\x12mission_raw_result\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.mission_raw.MissionRawResult\x12\x46\n\x13mission_import_data\x18\x02 \x01(\x0b\x32).mavsdk.rpc.mission_raw.MissionImportData\"1\n\x0fMissionProgress\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05\"\xd8\x01\n\x0bMissionItem\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\r\n\x05\x66rame\x18\x02 \x01(\r\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\r\x12\x0f\n\x07\x63urrent\x18\x04 \x01(\r\x12\x14\n\x0c\x61utocontinue\x18\x05 \x01(\r\x12\x0e\n\x06param1\x18\x06 \x01(\x02\x12\x0e\n\x06param2\x18\x07 \x01(\x02\x12\x0e\n\x06param3\x18\x08 \x01(\x02\x12\x0e\n\x06param4\x18\t \x01(\x02\x12\t\n\x01x\x18\n \x01(\x05\x12\t\n\x01y\x18\x0b \x01(\x05\x12\t\n\x01z\x18\x0c \x01(\x02\x12\x14\n\x0cmission_type\x18\r \x01(\r\"\xc6\x01\n\x11MissionImportData\x12:\n\rmission_items\x18\x01 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\x12;\n\x0egeofence_items\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\x12\x38\n\x0brally_items\x18\x03 \x03(\x0b\x32#.mavsdk.rpc.mission_raw.MissionItem\"\xfe\x04\n\x10MissionRawResult\x12?\n\x06result\x18\x01 \x01(\x0e\x32/.mavsdk.rpc.mission_raw.MissionRawResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x94\x04\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12!\n\x1dRESULT_TOO_MANY_MISSION_ITEMS\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x12\n\x0eRESULT_TIMEOUT\x10\x05\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x06\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x07\x12\x1f\n\x1bRESULT_NO_MISSION_AVAILABLE\x10\x08\x12\x1d\n\x19RESULT_TRANSFER_CANCELLED\x10\t\x12\"\n\x1eRESULT_FAILED_TO_OPEN_QGC_PLAN\x10\n\x12#\n\x1fRESULT_FAILED_TO_PARSE_QGC_PLAN\x10\x0b\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x0c\x12\x11\n\rRESULT_DENIED\x10\r\x12&\n\"RESULT_MISSION_TYPE_NOT_CONSISTENT\x10\x0e\x12\x1b\n\x17RESULT_INVALID_SEQUENCE\x10\x0f\x12\x1a\n\x16RESULT_CURRENT_INVALID\x10\x10\x12\x19\n\x15RESULT_PROTOCOL_ERROR\x10\x11\x12%\n!RESULT_INT_MESSAGES_NOT_SUPPORTED\x10\x12\x32\xbf\x0e\n\x11MissionRawService\x12n\n\rUploadMission\x12,.mavsdk.rpc.mission_raw.UploadMissionRequest\x1a-.mavsdk.rpc.mission_raw.UploadMissionResponse\"\x00\x12q\n\x0eUploadGeofence\x12-.mavsdk.rpc.mission_raw.UploadGeofenceRequest\x1a..mavsdk.rpc.mission_raw.UploadGeofenceResponse\"\x00\x12z\n\x11UploadRallyPoints\x12\x30.mavsdk.rpc.mission_raw.UploadRallyPointsRequest\x1a\x31.mavsdk.rpc.mission_raw.UploadRallyPointsResponse\"\x00\x12\x84\x01\n\x13\x43\x61ncelMissionUpload\x12\x32.mavsdk.rpc.mission_raw.CancelMissionUploadRequest\x1a\x33.mavsdk.rpc.mission_raw.CancelMissionUploadResponse\"\x04\x80\xb5\x18\x01\x12t\n\x0f\x44ownloadMission\x12..mavsdk.rpc.mission_raw.DownloadMissionRequest\x1a/.mavsdk.rpc.mission_raw.DownloadMissionResponse\"\x00\x12\x8a\x01\n\x15\x43\x61ncelMissionDownload\x12\x34.mavsdk.rpc.mission_raw.CancelMissionDownloadRequest\x1a\x35.mavsdk.rpc.mission_raw.CancelMissionDownloadResponse\"\x04\x80\xb5\x18\x01\x12k\n\x0cStartMission\x12+.mavsdk.rpc.mission_raw.StartMissionRequest\x1a,.mavsdk.rpc.mission_raw.StartMissionResponse\"\x00\x12k\n\x0cPauseMission\x12+.mavsdk.rpc.mission_raw.PauseMissionRequest\x1a,.mavsdk.rpc.mission_raw.PauseMissionResponse\"\x00\x12k\n\x0c\x43learMission\x12+.mavsdk.rpc.mission_raw.ClearMissionRequest\x1a,.mavsdk.rpc.mission_raw.ClearMissionResponse\"\x00\x12\x86\x01\n\x15SetCurrentMissionItem\x12\x34.mavsdk.rpc.mission_raw.SetCurrentMissionItemRequest\x1a\x35.mavsdk.rpc.mission_raw.SetCurrentMissionItemResponse\"\x00\x12\x88\x01\n\x18SubscribeMissionProgress\x12\x37.mavsdk.rpc.mission_raw.SubscribeMissionProgressRequest\x1a/.mavsdk.rpc.mission_raw.MissionProgressResponse\"\x00\x30\x01\x12\x89\x01\n\x17SubscribeMissionChanged\x12\x36.mavsdk.rpc.mission_raw.SubscribeMissionChangedRequest\x1a..mavsdk.rpc.mission_raw.MissionChangedResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x9c\x01\n\x1bImportQgroundcontrolMission\x12:.mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionRequest\x1a;.mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionResponse\"\x04\x80\xb5\x18\x01\x12\xba\x01\n%ImportQgroundcontrolMissionFromString\x12\x44.mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionFromStringRequest\x1a\x45.mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionFromStringResponse\"\x04\x80\xb5\x18\x01\x42(\n\x15io.mavsdk.mission_rawB\x0fMissionRawProtob\x06proto3')



_UPLOADMISSIONREQUEST = DESCRIPTOR.message_types_by_name['UploadMissionRequest']
_UPLOADMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['UploadMissionResponse']
_UPLOADGEOFENCEREQUEST = DESCRIPTOR.message_types_by_name['UploadGeofenceRequest']
_UPLOADGEOFENCERESPONSE = DESCRIPTOR.message_types_by_name['UploadGeofenceResponse']
_UPLOADRALLYPOINTSREQUEST = DESCRIPTOR.message_types_by_name['UploadRallyPointsRequest']
_UPLOADRALLYPOINTSRESPONSE = DESCRIPTOR.message_types_by_name['UploadRallyPointsResponse']
_CANCELMISSIONUPLOADREQUEST = DESCRIPTOR.message_types_by_name['CancelMissionUploadRequest']
_CANCELMISSIONUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['CancelMissionUploadResponse']
_DOWNLOADMISSIONREQUEST = DESCRIPTOR.message_types_by_name['DownloadMissionRequest']
_DOWNLOADMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['DownloadMissionResponse']
_CANCELMISSIONDOWNLOADREQUEST = DESCRIPTOR.message_types_by_name['CancelMissionDownloadRequest']
_CANCELMISSIONDOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name['CancelMissionDownloadResponse']
_STARTMISSIONREQUEST = DESCRIPTOR.message_types_by_name['StartMissionRequest']
_STARTMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['StartMissionResponse']
_PAUSEMISSIONREQUEST = DESCRIPTOR.message_types_by_name['PauseMissionRequest']
_PAUSEMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['PauseMissionResponse']
_CLEARMISSIONREQUEST = DESCRIPTOR.message_types_by_name['ClearMissionRequest']
_CLEARMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['ClearMissionResponse']
_SETCURRENTMISSIONITEMREQUEST = DESCRIPTOR.message_types_by_name['SetCurrentMissionItemRequest']
_SETCURRENTMISSIONITEMRESPONSE = DESCRIPTOR.message_types_by_name['SetCurrentMissionItemResponse']
_SUBSCRIBEMISSIONPROGRESSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeMissionProgressRequest']
_MISSIONPROGRESSRESPONSE = DESCRIPTOR.message_types_by_name['MissionProgressResponse']
_SUBSCRIBEMISSIONCHANGEDREQUEST = DESCRIPTOR.message_types_by_name['SubscribeMissionChangedRequest']
_MISSIONCHANGEDRESPONSE = DESCRIPTOR.message_types_by_name['MissionChangedResponse']
_IMPORTQGROUNDCONTROLMISSIONREQUEST = DESCRIPTOR.message_types_by_name['ImportQgroundcontrolMissionRequest']
_IMPORTQGROUNDCONTROLMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['ImportQgroundcontrolMissionResponse']
_IMPORTQGROUNDCONTROLMISSIONFROMSTRINGREQUEST = DESCRIPTOR.message_types_by_name['ImportQgroundcontrolMissionFromStringRequest']
_IMPORTQGROUNDCONTROLMISSIONFROMSTRINGRESPONSE = DESCRIPTOR.message_types_by_name['ImportQgroundcontrolMissionFromStringResponse']
_MISSIONPROGRESS = DESCRIPTOR.message_types_by_name['MissionProgress']
_MISSIONITEM = DESCRIPTOR.message_types_by_name['MissionItem']
_MISSIONIMPORTDATA = DESCRIPTOR.message_types_by_name['MissionImportData']
_MISSIONRAWRESULT = DESCRIPTOR.message_types_by_name['MissionRawResult']
_MISSIONRAWRESULT_RESULT = _MISSIONRAWRESULT.enum_types_by_name['Result']
UploadMissionRequest = _reflection.GeneratedProtocolMessageType('UploadMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMISSIONREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadMissionRequest)
  })
_sym_db.RegisterMessage(UploadMissionRequest)

UploadMissionResponse = _reflection.GeneratedProtocolMessageType('UploadMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMISSIONRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadMissionResponse)
  })
_sym_db.RegisterMessage(UploadMissionResponse)

UploadGeofenceRequest = _reflection.GeneratedProtocolMessageType('UploadGeofenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADGEOFENCEREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadGeofenceRequest)
  })
_sym_db.RegisterMessage(UploadGeofenceRequest)

UploadGeofenceResponse = _reflection.GeneratedProtocolMessageType('UploadGeofenceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADGEOFENCERESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadGeofenceResponse)
  })
_sym_db.RegisterMessage(UploadGeofenceResponse)

UploadRallyPointsRequest = _reflection.GeneratedProtocolMessageType('UploadRallyPointsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRALLYPOINTSREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadRallyPointsRequest)
  })
_sym_db.RegisterMessage(UploadRallyPointsRequest)

UploadRallyPointsResponse = _reflection.GeneratedProtocolMessageType('UploadRallyPointsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRALLYPOINTSRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.UploadRallyPointsResponse)
  })
_sym_db.RegisterMessage(UploadRallyPointsResponse)

CancelMissionUploadRequest = _reflection.GeneratedProtocolMessageType('CancelMissionUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONUPLOADREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionUploadRequest)
  })
_sym_db.RegisterMessage(CancelMissionUploadRequest)

CancelMissionUploadResponse = _reflection.GeneratedProtocolMessageType('CancelMissionUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONUPLOADRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionUploadResponse)
  })
_sym_db.RegisterMessage(CancelMissionUploadResponse)

DownloadMissionRequest = _reflection.GeneratedProtocolMessageType('DownloadMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMISSIONREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.DownloadMissionRequest)
  })
_sym_db.RegisterMessage(DownloadMissionRequest)

DownloadMissionResponse = _reflection.GeneratedProtocolMessageType('DownloadMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMISSIONRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.DownloadMissionResponse)
  })
_sym_db.RegisterMessage(DownloadMissionResponse)

CancelMissionDownloadRequest = _reflection.GeneratedProtocolMessageType('CancelMissionDownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONDOWNLOADREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionDownloadRequest)
  })
_sym_db.RegisterMessage(CancelMissionDownloadRequest)

CancelMissionDownloadResponse = _reflection.GeneratedProtocolMessageType('CancelMissionDownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONDOWNLOADRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.CancelMissionDownloadResponse)
  })
_sym_db.RegisterMessage(CancelMissionDownloadResponse)

StartMissionRequest = _reflection.GeneratedProtocolMessageType('StartMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTMISSIONREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.StartMissionRequest)
  })
_sym_db.RegisterMessage(StartMissionRequest)

StartMissionResponse = _reflection.GeneratedProtocolMessageType('StartMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTMISSIONRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.StartMissionResponse)
  })
_sym_db.RegisterMessage(StartMissionResponse)

PauseMissionRequest = _reflection.GeneratedProtocolMessageType('PauseMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEMISSIONREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.PauseMissionRequest)
  })
_sym_db.RegisterMessage(PauseMissionRequest)

PauseMissionResponse = _reflection.GeneratedProtocolMessageType('PauseMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEMISSIONRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.PauseMissionResponse)
  })
_sym_db.RegisterMessage(PauseMissionResponse)

ClearMissionRequest = _reflection.GeneratedProtocolMessageType('ClearMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEARMISSIONREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ClearMissionRequest)
  })
_sym_db.RegisterMessage(ClearMissionRequest)

ClearMissionResponse = _reflection.GeneratedProtocolMessageType('ClearMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLEARMISSIONRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ClearMissionResponse)
  })
_sym_db.RegisterMessage(ClearMissionResponse)

SetCurrentMissionItemRequest = _reflection.GeneratedProtocolMessageType('SetCurrentMissionItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETCURRENTMISSIONITEMREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SetCurrentMissionItemRequest)
  })
_sym_db.RegisterMessage(SetCurrentMissionItemRequest)

SetCurrentMissionItemResponse = _reflection.GeneratedProtocolMessageType('SetCurrentMissionItemResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETCURRENTMISSIONITEMRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SetCurrentMissionItemResponse)
  })
_sym_db.RegisterMessage(SetCurrentMissionItemResponse)

SubscribeMissionProgressRequest = _reflection.GeneratedProtocolMessageType('SubscribeMissionProgressRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEMISSIONPROGRESSREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SubscribeMissionProgressRequest)
  })
_sym_db.RegisterMessage(SubscribeMissionProgressRequest)

MissionProgressResponse = _reflection.GeneratedProtocolMessageType('MissionProgressResponse', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONPROGRESSRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionProgressResponse)
  })
_sym_db.RegisterMessage(MissionProgressResponse)

SubscribeMissionChangedRequest = _reflection.GeneratedProtocolMessageType('SubscribeMissionChangedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEMISSIONCHANGEDREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.SubscribeMissionChangedRequest)
  })
_sym_db.RegisterMessage(SubscribeMissionChangedRequest)

MissionChangedResponse = _reflection.GeneratedProtocolMessageType('MissionChangedResponse', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONCHANGEDRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionChangedResponse)
  })
_sym_db.RegisterMessage(MissionChangedResponse)

ImportQgroundcontrolMissionRequest = _reflection.GeneratedProtocolMessageType('ImportQgroundcontrolMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTQGROUNDCONTROLMISSIONREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionRequest)
  })
_sym_db.RegisterMessage(ImportQgroundcontrolMissionRequest)

ImportQgroundcontrolMissionResponse = _reflection.GeneratedProtocolMessageType('ImportQgroundcontrolMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTQGROUNDCONTROLMISSIONRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionResponse)
  })
_sym_db.RegisterMessage(ImportQgroundcontrolMissionResponse)

ImportQgroundcontrolMissionFromStringRequest = _reflection.GeneratedProtocolMessageType('ImportQgroundcontrolMissionFromStringRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTQGROUNDCONTROLMISSIONFROMSTRINGREQUEST,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionFromStringRequest)
  })
_sym_db.RegisterMessage(ImportQgroundcontrolMissionFromStringRequest)

ImportQgroundcontrolMissionFromStringResponse = _reflection.GeneratedProtocolMessageType('ImportQgroundcontrolMissionFromStringResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTQGROUNDCONTROLMISSIONFROMSTRINGRESPONSE,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.ImportQgroundcontrolMissionFromStringResponse)
  })
_sym_db.RegisterMessage(ImportQgroundcontrolMissionFromStringResponse)

MissionProgress = _reflection.GeneratedProtocolMessageType('MissionProgress', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONPROGRESS,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionProgress)
  })
_sym_db.RegisterMessage(MissionProgress)

MissionItem = _reflection.GeneratedProtocolMessageType('MissionItem', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONITEM,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionItem)
  })
_sym_db.RegisterMessage(MissionItem)

MissionImportData = _reflection.GeneratedProtocolMessageType('MissionImportData', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONIMPORTDATA,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionImportData)
  })
_sym_db.RegisterMessage(MissionImportData)

MissionRawResult = _reflection.GeneratedProtocolMessageType('MissionRawResult', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONRAWRESULT,
  '__module__' : 'mission_raw.mission_raw_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission_raw.MissionRawResult)
  })
_sym_db.RegisterMessage(MissionRawResult)

_MISSIONRAWSERVICE = DESCRIPTOR.services_by_name['MissionRawService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025io.mavsdk.mission_rawB\017MissionRawProto'
  _MISSIONRAWSERVICE.methods_by_name['CancelMissionUpload']._options = None
  _MISSIONRAWSERVICE.methods_by_name['CancelMissionUpload']._serialized_options = b'\200\265\030\001'
  _MISSIONRAWSERVICE.methods_by_name['CancelMissionDownload']._options = None
  _MISSIONRAWSERVICE.methods_by_name['CancelMissionDownload']._serialized_options = b'\200\265\030\001'
  _MISSIONRAWSERVICE.methods_by_name['SubscribeMissionChanged']._options = None
  _MISSIONRAWSERVICE.methods_by_name['SubscribeMissionChanged']._serialized_options = b'\200\265\030\000'
  _MISSIONRAWSERVICE.methods_by_name['ImportQgroundcontrolMission']._options = None
  _MISSIONRAWSERVICE.methods_by_name['ImportQgroundcontrolMission']._serialized_options = b'\200\265\030\001'
  _MISSIONRAWSERVICE.methods_by_name['ImportQgroundcontrolMissionFromString']._options = None
  _MISSIONRAWSERVICE.methods_by_name['ImportQgroundcontrolMissionFromString']._serialized_options = b'\200\265\030\001'
  _UPLOADMISSIONREQUEST._serialized_start=79
  _UPLOADMISSIONREQUEST._serialized_end=161
  _UPLOADMISSIONRESPONSE._serialized_start=163
  _UPLOADMISSIONRESPONSE._serialized_end=256
  _UPLOADGEOFENCEREQUEST._serialized_start=258
  _UPLOADGEOFENCEREQUEST._serialized_end=341
  _UPLOADGEOFENCERESPONSE._serialized_start=343
  _UPLOADGEOFENCERESPONSE._serialized_end=437
  _UPLOADRALLYPOINTSREQUEST._serialized_start=439
  _UPLOADRALLYPOINTSREQUEST._serialized_end=525
  _UPLOADRALLYPOINTSRESPONSE._serialized_start=527
  _UPLOADRALLYPOINTSRESPONSE._serialized_end=624
  _CANCELMISSIONUPLOADREQUEST._serialized_start=626
  _CANCELMISSIONUPLOADREQUEST._serialized_end=654
  _CANCELMISSIONUPLOADRESPONSE._serialized_start=656
  _CANCELMISSIONUPLOADRESPONSE._serialized_end=755
  _DOWNLOADMISSIONREQUEST._serialized_start=757
  _DOWNLOADMISSIONREQUEST._serialized_end=781
  _DOWNLOADMISSIONRESPONSE._serialized_start=784
  _DOWNLOADMISSIONRESPONSE._serialized_end=939
  _CANCELMISSIONDOWNLOADREQUEST._serialized_start=941
  _CANCELMISSIONDOWNLOADREQUEST._serialized_end=971
  _CANCELMISSIONDOWNLOADRESPONSE._serialized_start=973
  _CANCELMISSIONDOWNLOADRESPONSE._serialized_end=1074
  _STARTMISSIONREQUEST._serialized_start=1076
  _STARTMISSIONREQUEST._serialized_end=1097
  _STARTMISSIONRESPONSE._serialized_start=1099
  _STARTMISSIONRESPONSE._serialized_end=1191
  _PAUSEMISSIONREQUEST._serialized_start=1193
  _PAUSEMISSIONREQUEST._serialized_end=1214
  _PAUSEMISSIONRESPONSE._serialized_start=1216
  _PAUSEMISSIONRESPONSE._serialized_end=1308
  _CLEARMISSIONREQUEST._serialized_start=1310
  _CLEARMISSIONREQUEST._serialized_end=1331
  _CLEARMISSIONRESPONSE._serialized_start=1333
  _CLEARMISSIONRESPONSE._serialized_end=1425
  _SETCURRENTMISSIONITEMREQUEST._serialized_start=1427
  _SETCURRENTMISSIONITEMREQUEST._serialized_end=1472
  _SETCURRENTMISSIONITEMRESPONSE._serialized_start=1474
  _SETCURRENTMISSIONITEMRESPONSE._serialized_end=1575
  _SUBSCRIBEMISSIONPROGRESSREQUEST._serialized_start=1577
  _SUBSCRIBEMISSIONPROGRESSREQUEST._serialized_end=1610
  _MISSIONPROGRESSRESPONSE._serialized_start=1612
  _MISSIONPROGRESSRESPONSE._serialized_end=1704
  _SUBSCRIBEMISSIONCHANGEDREQUEST._serialized_start=1706
  _SUBSCRIBEMISSIONCHANGEDREQUEST._serialized_end=1738
  _MISSIONCHANGEDRESPONSE._serialized_start=1740
  _MISSIONCHANGEDRESPONSE._serialized_end=1789
  _IMPORTQGROUNDCONTROLMISSIONREQUEST._serialized_start=1791
  _IMPORTQGROUNDCONTROLMISSIONREQUEST._serialized_end=1850
  _IMPORTQGROUNDCONTROLMISSIONRESPONSE._serialized_start=1853
  _IMPORTQGROUNDCONTROLMISSIONRESPONSE._serialized_end=2032
  _IMPORTQGROUNDCONTROLMISSIONFROMSTRINGREQUEST._serialized_start=2034
  _IMPORTQGROUNDCONTROLMISSIONFROMSTRINGREQUEST._serialized_end=2098
  _IMPORTQGROUNDCONTROLMISSIONFROMSTRINGRESPONSE._serialized_start=2101
  _IMPORTQGROUNDCONTROLMISSIONFROMSTRINGRESPONSE._serialized_end=2290
  _MISSIONPROGRESS._serialized_start=2292
  _MISSIONPROGRESS._serialized_end=2341
  _MISSIONITEM._serialized_start=2344
  _MISSIONITEM._serialized_end=2560
  _MISSIONIMPORTDATA._serialized_start=2563
  _MISSIONIMPORTDATA._serialized_end=2761
  _MISSIONRAWRESULT._serialized_start=2764
  _MISSIONRAWRESULT._serialized_end=3402
  _MISSIONRAWRESULT_RESULT._serialized_start=2870
  _MISSIONRAWRESULT_RESULT._serialized_end=3402
  _MISSIONRAWSERVICE._serialized_start=3405
  _MISSIONRAWSERVICE._serialized_end=5260
# @@protoc_insertion_point(module_scope)