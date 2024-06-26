"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/planning_msgs/pad_msg.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/modules/common_msgs/planning_msgs/pad_msg.proto\x12\x0fapollo.planning\x1a+modules/common_msgs/basic_msgs/header.proto"\xe4\x01\n\nPadMessage\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x129\n\x06action\x18\x02 \x01(\x0e2).apollo.planning.PadMessage.DrivingAction"t\n\rDrivingAction\x12\x08\n\x04NONE\x10d\x12\n\n\x06FOLLOW\x10\x00\x12\x0f\n\x0bCHANGE_LEFT\x10\x01\x12\x10\n\x0cCHANGE_RIGHT\x10\x02\x12\r\n\tPULL_OVER\x10\x03\x12\x08\n\x04STOP\x10\x04\x12\x11\n\rRESUME_CRUISE\x10\x05',
    dependencies=[modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR],
)
_PADMESSAGE_DRIVINGACTION = _descriptor.EnumDescriptor(
    name="DrivingAction",
    full_name="apollo.planning.PadMessage.DrivingAction",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NONE",
            index=0,
            number=100,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FOLLOW",
            index=1,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANGE_LEFT",
            index=2,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANGE_RIGHT",
            index=3,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PULL_OVER",
            index=4,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP",
            index=5,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RESUME_CRUISE",
            index=6,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=226,
    serialized_end=342,
)
_sym_db.RegisterEnumDescriptor(_PADMESSAGE_DRIVINGACTION)
_PADMESSAGE = _descriptor.Descriptor(
    name="PadMessage",
    full_name="apollo.planning.PadMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.planning.PadMessage.header",
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
            name="action",
            full_name="apollo.planning.PadMessage.action",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=100,
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
    enum_types=[_PADMESSAGE_DRIVINGACTION],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=114,
    serialized_end=342,
)
_PADMESSAGE.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_PADMESSAGE.fields_by_name["action"].enum_type = _PADMESSAGE_DRIVINGACTION
_PADMESSAGE_DRIVINGACTION.containing_type = _PADMESSAGE
DESCRIPTOR.message_types_by_name["PadMessage"] = _PADMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PadMessage = _reflection.GeneratedProtocolMessageType(
    "PadMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _PADMESSAGE,
        "__module__": "modules.common_msgs.planning_msgs.pad_msg_pb2",
    },
)
_sym_db.RegisterMessage(PadMessage)
