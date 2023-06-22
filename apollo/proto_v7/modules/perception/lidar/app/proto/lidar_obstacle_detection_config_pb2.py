"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/lidar/app/proto/lidar_obstacle_detection_config.proto",
    package="apollo.perception.lidar",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\nHmodules/perception/lidar/app/proto/lidar_obstacle_detection_config.proto\x12\x17apollo.perception.lidar\"\xba\x01\n\x1cLidarObstacleDetectionConfig\x12,\n\x0cpreprocessor\x18\x01 \x01(\t:\x16PointCloudPreprocessor\x12'\n\x08detector\x18\x02 \x01(\t:\x15PointPillarsDetection\x12\x1d\n\x0fuse_map_manager\x18\x03 \x01(\x08:\x04true\x12$\n\x16use_object_filter_bank\x18\x04 \x01(\x08:\x04true",
)
_LIDAROBSTACLEDETECTIONCONFIG = _descriptor.Descriptor(
    name="LidarObstacleDetectionConfig",
    full_name="apollo.perception.lidar.LidarObstacleDetectionConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="preprocessor",
            full_name="apollo.perception.lidar.LidarObstacleDetectionConfig.preprocessor",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"PointCloudPreprocessor".decode("utf-8"),
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
            name="detector",
            full_name="apollo.perception.lidar.LidarObstacleDetectionConfig.detector",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"PointPillarsDetection".decode("utf-8"),
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
            name="use_map_manager",
            full_name="apollo.perception.lidar.LidarObstacleDetectionConfig.use_map_manager",
            index=2,
            number=3,
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
            name="use_object_filter_bank",
            full_name="apollo.perception.lidar.LidarObstacleDetectionConfig.use_object_filter_bank",
            index=3,
            number=4,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=102,
    serialized_end=288,
)
DESCRIPTOR.message_types_by_name[
    "LidarObstacleDetectionConfig"
] = _LIDAROBSTACLEDETECTIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
LidarObstacleDetectionConfig = _reflection.GeneratedProtocolMessageType(
    "LidarObstacleDetectionConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _LIDAROBSTACLEDETECTIONCONFIG,
        "__module__": "modules.perception.lidar.app.proto.lidar_obstacle_detection_config_pb2",
    },
)
_sym_db.RegisterMessage(LidarObstacleDetectionConfig)
