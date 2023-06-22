"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from .....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from .....modules.drivers.microphone.proto import (
    microphone_config_pb2 as modules_dot_drivers_dot_microphone_dot_proto_dot_microphone__config__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/microphone/proto/audio.proto",
    package="apollo.drivers.microphone.config",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n,modules/drivers/microphone/proto/audio.proto\x12 apollo.drivers.microphone.config\x1a!modules/common/proto/header.proto\x1a8modules/drivers/microphone/proto/microphone_config.proto"`\n\x0bChannelData\x12C\n\x0cchannel_type\x18\x01 \x01(\x0e2-.apollo.drivers.microphone.config.ChannelType\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\xc6\x01\n\tAudioData\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12M\n\x11microphone_config\x18\x02 \x01(\x0b22.apollo.drivers.microphone.config.MicrophoneConfig\x12C\n\x0cchannel_data\x18\x03 \x03(\x0b2-.apollo.drivers.microphone.config.ChannelData',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_drivers_dot_microphone_dot_proto_dot_microphone__config__pb2.DESCRIPTOR,
    ],
)
_CHANNELDATA = _descriptor.Descriptor(
    name="ChannelData",
    full_name="apollo.drivers.microphone.config.ChannelData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="channel_type",
            full_name="apollo.drivers.microphone.config.ChannelData.channel_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="apollo.drivers.microphone.config.ChannelData.data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=175,
    serialized_end=271,
)
_AUDIODATA = _descriptor.Descriptor(
    name="AudioData",
    full_name="apollo.drivers.microphone.config.AudioData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.drivers.microphone.config.AudioData.header",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="microphone_config",
            full_name="apollo.drivers.microphone.config.AudioData.microphone_config",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="channel_data",
            full_name="apollo.drivers.microphone.config.AudioData.channel_data",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=274,
    serialized_end=472,
)
_CHANNELDATA.fields_by_name[
    "channel_type"
].enum_type = (
    modules_dot_drivers_dot_microphone_dot_proto_dot_microphone__config__pb2._CHANNELTYPE
)
_AUDIODATA.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_AUDIODATA.fields_by_name[
    "microphone_config"
].message_type = (
    modules_dot_drivers_dot_microphone_dot_proto_dot_microphone__config__pb2._MICROPHONECONFIG
)
_AUDIODATA.fields_by_name["channel_data"].message_type = _CHANNELDATA
DESCRIPTOR.message_types_by_name["ChannelData"] = _CHANNELDATA
DESCRIPTOR.message_types_by_name["AudioData"] = _AUDIODATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ChannelData = _reflection.GeneratedProtocolMessageType(
    "ChannelData",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHANNELDATA,
        "__module__": "modules.drivers.microphone.proto.audio_pb2",
    },
)
_sym_db.RegisterMessage(ChannelData)
AudioData = _reflection.GeneratedProtocolMessageType(
    "AudioData",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUDIODATA,
        "__module__": "modules.drivers.microphone.proto.audio_pb2",
    },
)
_sym_db.RegisterMessage(AudioData)
