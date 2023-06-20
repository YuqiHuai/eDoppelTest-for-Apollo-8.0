"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.audio_msgs import (
    audio_common_pb2 as modules_dot_common__msgs_dot_audio__msgs_dot_audio__common__pb2,
)
from ....modules.common_msgs.basic_msgs import (
    geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2,
)
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/audio_msgs/audio.proto",
    package="apollo.audio",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n*modules/common_msgs/audio_msgs/audio.proto\x12\x0capollo.audio\x1a1modules/common_msgs/audio_msgs/audio_common.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto"\xc6\x01\n\x0eAudioDetection\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x10\n\x08is_siren\x18\x02 \x01(\x08\x12:\n\rmoving_result\x18\x03 \x01(\x0e2\x1a.apollo.audio.MovingResult:\x07UNKNOWN\x12(\n\x08position\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12\x15\n\rsource_degree\x18\x05 \x01(\x01',
    dependencies=[
        modules_dot_common__msgs_dot_audio__msgs_dot_audio__common__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,
    ],
)
_AUDIODETECTION = _descriptor.Descriptor(
    name="AudioDetection",
    full_name="apollo.audio.AudioDetection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.audio.AudioDetection.header",
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
            name="is_siren",
            full_name="apollo.audio.AudioDetection.is_siren",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="moving_result",
            full_name="apollo.audio.AudioDetection.moving_result",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=True,
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
            name="position",
            full_name="apollo.audio.AudioDetection.position",
            index=3,
            number=4,
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
            name="source_degree",
            full_name="apollo.audio.AudioDetection.source_degree",
            index=4,
            number=5,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_start=204,
    serialized_end=402,
)
_AUDIODETECTION.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_AUDIODETECTION.fields_by_name[
    "moving_result"
].enum_type = (
    modules_dot_common__msgs_dot_audio__msgs_dot_audio__common__pb2._MOVINGRESULT
)
_AUDIODETECTION.fields_by_name[
    "position"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2._POINT3D
DESCRIPTOR.message_types_by_name["AudioDetection"] = _AUDIODETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
AudioDetection = _reflection.GeneratedProtocolMessageType(
    "AudioDetection",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUDIODETECTION,
        "__module__": "modules.common_msgs.audio_msgs.audio_pb2",
    },
)
_sym_db.RegisterMessage(AudioDetection)
