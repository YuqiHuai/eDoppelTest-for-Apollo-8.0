"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from .....modules.drivers.lidar.proto import (
    hesai_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2,
)
from .....modules.drivers.lidar.proto import (
    lidar_parameter_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2,
)
from .....modules.drivers.lidar.proto import (
    robosense_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2,
)
from .....modules.drivers.lidar.proto import (
    velodyne_config_pb2 as modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/lidar/proto/config.proto",
    package="apollo.drivers.lidar",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n(modules/drivers/lidar/proto/config.proto\x12\x14apollo.drivers.lidar\x1a.modules/drivers/lidar/proto/hesai_config.proto\x1a1modules/drivers/lidar/proto/velodyne_config.proto\x1a1modules/drivers/lidar/proto/lidar_parameter.proto\x1a2modules/drivers/lidar/proto/robosense_config.proto"\xdd\x01\n\x06config\x12>\n\x05brand\x18\x01 \x01(\x0e2/.apollo.drivers.lidar.LidarParameter.LidarBrand\x12+\n\x05hesai\x18\x02 \x01(\x0b2\x1c.apollo.drivers.hesai.Config\x123\n\trobosense\x18\x03 \x01(\x0b2 .apollo.drivers.robosense.Config\x121\n\x08velodyne\x18\x04 \x01(\x0b2\x1f.apollo.drivers.velodyne.Config',
    dependencies=[
        modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2.DESCRIPTOR,
        modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2.DESCRIPTOR,
        modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2.DESCRIPTOR,
        modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2.DESCRIPTOR,
    ],
)
_CONFIG = _descriptor.Descriptor(
    name="config",
    full_name="apollo.drivers.lidar.config",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="brand",
            full_name="apollo.drivers.lidar.config.brand",
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
            name="hesai",
            full_name="apollo.drivers.lidar.config.hesai",
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
            name="robosense",
            full_name="apollo.drivers.lidar.config.robosense",
            index=2,
            number=3,
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
            name="velodyne",
            full_name="apollo.drivers.lidar.config.velodyne",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=269,
    serialized_end=490,
)
_CONFIG.fields_by_name[
    "brand"
].enum_type = (
    modules_dot_drivers_dot_lidar_dot_proto_dot_lidar__parameter__pb2._LIDARPARAMETER_LIDARBRAND
)
_CONFIG.fields_by_name[
    "hesai"
].message_type = modules_dot_drivers_dot_lidar_dot_proto_dot_hesai__config__pb2._CONFIG
_CONFIG.fields_by_name[
    "robosense"
].message_type = (
    modules_dot_drivers_dot_lidar_dot_proto_dot_robosense__config__pb2._CONFIG
)
_CONFIG.fields_by_name[
    "velodyne"
].message_type = (
    modules_dot_drivers_dot_lidar_dot_proto_dot_velodyne__config__pb2._CONFIG
)
DESCRIPTOR.message_types_by_name["config"] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
config = _reflection.GeneratedProtocolMessageType(
    "config",
    (_message.Message,),
    {"DESCRIPTOR": _CONFIG, "__module__": "modules.drivers.lidar.proto.config_pb2"},
)
_sym_db.RegisterMessage(config)
