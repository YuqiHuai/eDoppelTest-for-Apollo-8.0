"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/proto/dst_existence_fusion_config.proto",
    package="apollo.perception",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n:modules/perception/proto/dst_existence_fusion_config.proto\x12\x11apollo.perception"?\n\x0fCameraValidDist\x12\x15\n\x0bcamera_name\x18\x01 \x01(\t:\x00\x12\x15\n\nvalid_dist\x18\x02 \x01(\x01:\x010"\x85\x01\n\x18DstExistenceFusionConfig\x12*\n\x1ftrack_object_max_match_distance\x18\x01 \x01(\x01:\x014\x12=\n\x11camera_valid_dist\x18\x02 \x03(\x0b2".apollo.perception.CameraValidDist',
)
_CAMERAVALIDDIST = _descriptor.Descriptor(
    name="CameraValidDist",
    full_name="apollo.perception.CameraValidDist",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="camera_name",
            full_name="apollo.perception.CameraValidDist.camera_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"".decode("utf-8"),
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
            name="valid_dist",
            full_name="apollo.perception.CameraValidDist.valid_dist",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
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
    serialized_start=81,
    serialized_end=144,
)
_DSTEXISTENCEFUSIONCONFIG = _descriptor.Descriptor(
    name="DstExistenceFusionConfig",
    full_name="apollo.perception.DstExistenceFusionConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="track_object_max_match_distance",
            full_name="apollo.perception.DstExistenceFusionConfig.track_object_max_match_distance",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(4),
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
            name="camera_valid_dist",
            full_name="apollo.perception.DstExistenceFusionConfig.camera_valid_dist",
            index=1,
            number=2,
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
    serialized_start=147,
    serialized_end=280,
)
_DSTEXISTENCEFUSIONCONFIG.fields_by_name[
    "camera_valid_dist"
].message_type = _CAMERAVALIDDIST
DESCRIPTOR.message_types_by_name["CameraValidDist"] = _CAMERAVALIDDIST
DESCRIPTOR.message_types_by_name["DstExistenceFusionConfig"] = _DSTEXISTENCEFUSIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CameraValidDist = _reflection.GeneratedProtocolMessageType(
    "CameraValidDist",
    (_message.Message,),
    {
        "DESCRIPTOR": _CAMERAVALIDDIST,
        "__module__": "modules.perception.proto.dst_existence_fusion_config_pb2",
    },
)
_sym_db.RegisterMessage(CameraValidDist)
DstExistenceFusionConfig = _reflection.GeneratedProtocolMessageType(
    "DstExistenceFusionConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _DSTEXISTENCEFUSIONCONFIG,
        "__module__": "modules.perception.proto.dst_existence_fusion_config_pb2",
    },
)
_sym_db.RegisterMessage(DstExistenceFusionConfig)
