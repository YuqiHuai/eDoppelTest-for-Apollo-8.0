"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/task_manager/proto/task_manager_config.proto",
    package="apollo.task_manager",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n4modules/task_manager/proto/task_manager_config.proto\x12\x13apollo.task_manager"\x85\x01\n\x0bTopicConfig\x12\x1d\n\x15routing_request_topic\x18\x01 \x01(\t\x12\x1e\n\x16routing_response_topic\x18\x02 \x01(\t\x12\x1f\n\x17localization_pose_topic\x18\x03 \x01(\t\x12\x16\n\x0eplanning_topic\x18\x04 \x01(\t"K\n\x11TaskManagerConfig\x126\n\x0ctopic_config\x18\x01 \x01(\x0b2 .apollo.task_manager.TopicConfig',
)
_TOPICCONFIG = _descriptor.Descriptor(
    name="TopicConfig",
    full_name="apollo.task_manager.TopicConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="routing_request_topic",
            full_name="apollo.task_manager.TopicConfig.routing_request_topic",
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
            name="routing_response_topic",
            full_name="apollo.task_manager.TopicConfig.routing_response_topic",
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
            name="localization_pose_topic",
            full_name="apollo.task_manager.TopicConfig.localization_pose_topic",
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
            name="planning_topic",
            full_name="apollo.task_manager.TopicConfig.planning_topic",
            index=3,
            number=4,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=78,
    serialized_end=211,
)
_TASKMANAGERCONFIG = _descriptor.Descriptor(
    name="TaskManagerConfig",
    full_name="apollo.task_manager.TaskManagerConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="topic_config",
            full_name="apollo.task_manager.TaskManagerConfig.topic_config",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=213,
    serialized_end=288,
)
_TASKMANAGERCONFIG.fields_by_name["topic_config"].message_type = _TOPICCONFIG
DESCRIPTOR.message_types_by_name["TopicConfig"] = _TOPICCONFIG
DESCRIPTOR.message_types_by_name["TaskManagerConfig"] = _TASKMANAGERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
TopicConfig = _reflection.GeneratedProtocolMessageType(
    "TopicConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOPICCONFIG,
        "__module__": "modules.task_manager.proto.task_manager_config_pb2",
    },
)
_sym_db.RegisterMessage(TopicConfig)
TaskManagerConfig = _reflection.GeneratedProtocolMessageType(
    "TaskManagerConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASKMANAGERCONFIG,
        "__module__": "modules.task_manager.proto.task_manager_config_pb2",
    },
)
_sym_db.RegisterMessage(TaskManagerConfig)
