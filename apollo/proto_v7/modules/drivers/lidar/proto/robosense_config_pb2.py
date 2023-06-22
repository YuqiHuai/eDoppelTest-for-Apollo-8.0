"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/lidar/proto/robosense_config.proto",
    package="apollo.drivers.robosense",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2modules/drivers/lidar/proto/robosense_config.proto\x12\x18apollo.drivers.robosense"\xbb\x02\n\x06Config\x12\r\n\x05model\x18\x01 \x01(\t\x12\x10\n\x08frame_id\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x11\n\tmsop_port\x18\x04 \x01(\r\x12\x12\n\ndifop_port\x18\x05 \x01(\r\x12\x11\n\techo_mode\x18\x06 \x01(\r\x12\x13\n\x0bstart_angle\x18\x08 \x01(\r\x12\x11\n\tend_angle\x18\t \x01(\r\x12\x14\n\x0cmin_distance\x18\n \x01(\r\x12\x14\n\x0cmax_distance\x18\x0b \x01(\r\x12\x11\n\tcut_angle\x18\x0c \x01(\r\x12\x1a\n\x12pointcloud_channel\x18\r \x01(\t\x12\x14\n\x0cscan_channel\x18\x0e \x01(\t\x12\x18\n\x10calibration_file\x18\x0f \x01(\t\x12\x17\n\x0fuse_lidar_clock\x18\x10 \x01(\x08',
)
_CONFIG = _descriptor.Descriptor(
    name="Config",
    full_name="apollo.drivers.robosense.Config",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="model",
            full_name="apollo.drivers.robosense.Config.model",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="frame_id",
            full_name="apollo.drivers.robosense.Config.frame_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="ip",
            full_name="apollo.drivers.robosense.Config.ip",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="msop_port",
            full_name="apollo.drivers.robosense.Config.msop_port",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
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
            name="difop_port",
            full_name="apollo.drivers.robosense.Config.difop_port",
            index=4,
            number=5,
            type=13,
            cpp_type=3,
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
            name="echo_mode",
            full_name="apollo.drivers.robosense.Config.echo_mode",
            index=5,
            number=6,
            type=13,
            cpp_type=3,
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
            name="start_angle",
            full_name="apollo.drivers.robosense.Config.start_angle",
            index=6,
            number=8,
            type=13,
            cpp_type=3,
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
            name="end_angle",
            full_name="apollo.drivers.robosense.Config.end_angle",
            index=7,
            number=9,
            type=13,
            cpp_type=3,
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
            name="min_distance",
            full_name="apollo.drivers.robosense.Config.min_distance",
            index=8,
            number=10,
            type=13,
            cpp_type=3,
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
            name="max_distance",
            full_name="apollo.drivers.robosense.Config.max_distance",
            index=9,
            number=11,
            type=13,
            cpp_type=3,
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
            name="cut_angle",
            full_name="apollo.drivers.robosense.Config.cut_angle",
            index=10,
            number=12,
            type=13,
            cpp_type=3,
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
            name="pointcloud_channel",
            full_name="apollo.drivers.robosense.Config.pointcloud_channel",
            index=11,
            number=13,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="scan_channel",
            full_name="apollo.drivers.robosense.Config.scan_channel",
            index=12,
            number=14,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="calibration_file",
            full_name="apollo.drivers.robosense.Config.calibration_file",
            index=13,
            number=15,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="use_lidar_clock",
            full_name="apollo.drivers.robosense.Config.use_lidar_clock",
            index=14,
            number=16,
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
    serialized_end=396,
)
DESCRIPTOR.message_types_by_name["Config"] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Config = _reflection.GeneratedProtocolMessageType(
    "Config",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONFIG,
        "__module__": "modules.drivers.lidar.proto.robosense_config_pb2",
    },
)
_sym_db.RegisterMessage(Config)
