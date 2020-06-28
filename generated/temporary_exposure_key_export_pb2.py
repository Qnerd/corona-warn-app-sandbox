# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/cwa-server/common/protocols/target/classes/app/coronawarn/server/common/protocols/external/exposurenotification/temporary_exposure_key_export.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/cwa-server/common/protocols/target/classes/app/coronawarn/server/common/protocols/external/exposurenotification/temporary_exposure_key_export.proto',
  package='app.coronawarn.server.common.protocols.external.exposurenotification',
  syntax='proto2',
  serialized_pb=_b('\n\x97\x01src/cwa-server/common/protocols/target/classes/app/coronawarn/server/common/protocols/external/exposurenotification/temporary_exposure_key_export.proto\x12\x44\x61pp.coronawarn.server.common.protocols.external.exposurenotification\"\xdb\x02\n\x1aTemporaryExposureKeyExport\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x06\x12\x15\n\rend_timestamp\x18\x02 \x01(\x06\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x11\n\tbatch_num\x18\x04 \x01(\x05\x12\x12\n\nbatch_size\x18\x05 \x01(\x05\x12l\n\x0fsignature_infos\x18\x06 \x03(\x0b\x32S.app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo\x12h\n\x04keys\x18\x07 \x03(\x0b\x32Z.app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey\"\x9b\x01\n\rSignatureInfo\x12\x15\n\rapp_bundle_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61ndroid_package\x18\x02 \x01(\t\x12 \n\x18verification_key_version\x18\x03 \x01(\t\x12\x1b\n\x13verification_key_id\x18\x04 \x01(\t\x12\x1b\n\x13signature_algorithm\x18\x05 \x01(\t\"\x8d\x01\n\x14TemporaryExposureKey\x12\x10\n\x08key_data\x18\x01 \x01(\x0c\x12\x1f\n\x17transmission_risk_level\x18\x02 \x01(\x05\x12%\n\x1drolling_start_interval_number\x18\x03 \x01(\x05\x12\x1b\n\x0erolling_period\x18\x04 \x01(\x05:\x03\x31\x34\x34\x42H\nDapp.coronawarn.server.common.protocols.external.exposurenotificationP\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TEMPORARYEXPOSUREKEYEXPORT = _descriptor.Descriptor(
  name='TemporaryExposureKeyExport',
  full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.start_timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.end_timestamp', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='region', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.region', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_num', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.batch_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.batch_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature_infos', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.signature_infos', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport.keys', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=574,
)


_SIGNATUREINFO = _descriptor.Descriptor(
  name='SignatureInfo',
  full_name='app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_bundle_id', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo.app_bundle_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='android_package', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo.android_package', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verification_key_version', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo.verification_key_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verification_key_id', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo.verification_key_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature_algorithm', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo.signature_algorithm', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=732,
)


_TEMPORARYEXPOSUREKEY = _descriptor.Descriptor(
  name='TemporaryExposureKey',
  full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_data', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey.key_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transmission_risk_level', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey.transmission_risk_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rolling_start_interval_number', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey.rolling_start_interval_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rolling_period', full_name='app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey.rolling_period', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=144,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=876,
)

_TEMPORARYEXPOSUREKEYEXPORT.fields_by_name['signature_infos'].message_type = _SIGNATUREINFO
_TEMPORARYEXPOSUREKEYEXPORT.fields_by_name['keys'].message_type = _TEMPORARYEXPOSUREKEY
DESCRIPTOR.message_types_by_name['TemporaryExposureKeyExport'] = _TEMPORARYEXPOSUREKEYEXPORT
DESCRIPTOR.message_types_by_name['SignatureInfo'] = _SIGNATUREINFO
DESCRIPTOR.message_types_by_name['TemporaryExposureKey'] = _TEMPORARYEXPOSUREKEY

TemporaryExposureKeyExport = _reflection.GeneratedProtocolMessageType('TemporaryExposureKeyExport', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORARYEXPOSUREKEYEXPORT,
  __module__ = 'src.cwa_server.common.protocols.target.classes.app.coronawarn.server.common.protocols.external.exposurenotification.temporary_exposure_key_export_pb2'
  # @@protoc_insertion_point(class_scope:app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKeyExport)
  ))
_sym_db.RegisterMessage(TemporaryExposureKeyExport)

SignatureInfo = _reflection.GeneratedProtocolMessageType('SignatureInfo', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATUREINFO,
  __module__ = 'src.cwa_server.common.protocols.target.classes.app.coronawarn.server.common.protocols.external.exposurenotification.temporary_exposure_key_export_pb2'
  # @@protoc_insertion_point(class_scope:app.coronawarn.server.common.protocols.external.exposurenotification.SignatureInfo)
  ))
_sym_db.RegisterMessage(SignatureInfo)

TemporaryExposureKey = _reflection.GeneratedProtocolMessageType('TemporaryExposureKey', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORARYEXPOSUREKEY,
  __module__ = 'src.cwa_server.common.protocols.target.classes.app.coronawarn.server.common.protocols.external.exposurenotification.temporary_exposure_key_export_pb2'
  # @@protoc_insertion_point(class_scope:app.coronawarn.server.common.protocols.external.exposurenotification.TemporaryExposureKey)
  ))
_sym_db.RegisterMessage(TemporaryExposureKey)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\nDapp.coronawarn.server.common.protocols.external.exposurenotificationP\001'))
# @@protoc_insertion_point(module_scope)
