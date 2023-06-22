"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from .....modules.drivers.lidar.proto import (
    hesai_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/lidar/proto/hesai_config.proto",
    package="apollo.drivers.hesai",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n.modules/drivers/lidar/proto/hesai_config.proto\x12\x14apollo.drivers.hesai\x1a'modules/drivers/lidar/proto/hesai.proto\"\xc6\x02\n\x06Config\x12*\n\x05model\x18\x01 \x01(\x0e2\x1b.apollo.drivers.hesai.Model\x12\x19\n\x02ip\x18\x02 \x01(\t:\r192.168.20.13\x12\x17\n\x0flidar_recv_port\x18\x03 \x01(\r\x12\x15\n\rgps_recv_port\x18\x04 \x01(\r\x12\x13\n\x0bstart_angle\x18\x05 \x01(\r\x12\x1a\n\x12pointcloud_channel\x18\x06 \x01(\t\x12\x11\n\ttime_zone\x18\x07 \x01(\r\x12\x10\n\x08frame_id\x18\x08 \x01(\t\x12\x14\n\x0cscan_channel\x18\t \x01(\t\x12#\n\x15is_online_calibration\x18\x0b \x01(\x08:\x04true\x12\x18\n\x10calibration_file\x18\x0c \x01(\t\x12\x1a\n\x0ctcp_cmd_port\x18\r \x01(\r:\x049347",
    dependencies=[modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__pb2.DESCRIPTOR],
)
_CONFIG = _descriptor.Descriptor(
    name="Config",
    full_name="apollo.drivers.hesai.Config",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="model",
            full_name="apollo.drivers.hesai.Config.model",
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
            name="ip",
            full_name="apollo.drivers.hesai.Config.ip",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"192.168.20.13".decode("utf-8"),
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
            name="lidar_recv_port",
            full_name="apollo.drivers.hesai.Config.lidar_recv_port",
            index=2,
            number=3,
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
            name="gps_recv_port",
            full_name="apollo.drivers.hesai.Config.gps_recv_port",
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
            name="start_angle",
            full_name="apollo.drivers.hesai.Config.start_angle",
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
            name="pointcloud_channel",
            full_name="apollo.drivers.hesai.Config.pointcloud_channel",
            index=5,
            number=6,
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
            name="time_zone",
            full_name="apollo.drivers.hesai.Config.time_zone",
            index=6,
            number=7,
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
            name="frame_id",
            full_name="apollo.drivers.hesai.Config.frame_id",
            index=7,
            number=8,
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
            full_name="apollo.drivers.hesai.Config.scan_channel",
            index=8,
            number=9,
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
            name="is_online_calibration",
            full_name="apollo.drivers.hesai.Config.is_online_calibration",
            index=9,
            number=11,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=True,
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
            full_name="apollo.drivers.hesai.Config.calibration_file",
            index=10,
            number=12,
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
            name="tcp_cmd_port",
            full_name="apollo.drivers.hesai.Config.tcp_cmd_port",
            index=11,
            number=13,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=True,
            default_value=9347,
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
    serialized_start=114,
    serialized_end=440,
)
_CONFIG.fields_by_name[
    "model"
].enum_type = modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__pb2._MODEL
DESCRIPTOR.message_types_by_name["Config"] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Config = _reflection.GeneratedProtocolMessageType(
    "Config",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONFIG,
        "__module__": "modules.drivers.lidar.proto.hesai_config_pb2",
    },
)
_sym_db.RegisterMessage(Config)
