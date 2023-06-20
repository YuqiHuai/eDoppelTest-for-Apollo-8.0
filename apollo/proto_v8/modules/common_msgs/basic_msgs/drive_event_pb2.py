"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)
from ....modules.common_msgs.localization_msgs import (
    pose_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_pose__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/basic_msgs/drive_event.proto",
    package="apollo.common",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n0modules/common_msgs/basic_msgs/drive_event.proto\x12\rapollo.common\x1a+modules/common_msgs/basic_msgs/header.proto\x1a0modules/common_msgs/localization_msgs/pose.proto"\xf6\x01\n\nDriveEvent\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\r\n\x05event\x18\x02 \x01(\t\x12+\n\x08location\x18\x03 \x01(\x0b2\x19.apollo.localization.Pose\x12,\n\x04type\x18\x04 \x03(\x0e2\x1e.apollo.common.DriveEvent.Type\x12\x15\n\ris_reportable\x18\x05 \x01(\x08"@\n\x04Type\x12\x0c\n\x08CRITICAL\x10\x00\x12\x0b\n\x07PROBLEM\x10\x01\x12\x0b\n\x07DESIRED\x10\x02\x12\x10\n\x0cOUT_OF_SCOPE\x10\x03',
    dependencies=[
        modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_localization__msgs_dot_pose__pb2.DESCRIPTOR,
    ],
)
_DRIVEEVENT_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.common.DriveEvent.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CRITICAL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PROBLEM",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DESIRED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OUT_OF_SCOPE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=345,
    serialized_end=409,
)
_sym_db.RegisterEnumDescriptor(_DRIVEEVENT_TYPE)
_DRIVEEVENT = _descriptor.Descriptor(
    name="DriveEvent",
    full_name="apollo.common.DriveEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.common.DriveEvent.header",
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
            name="event",
            full_name="apollo.common.DriveEvent.event",
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
            name="location",
            full_name="apollo.common.DriveEvent.location",
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
            name="type",
            full_name="apollo.common.DriveEvent.type",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
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
        _descriptor.FieldDescriptor(
            name="is_reportable",
            full_name="apollo.common.DriveEvent.is_reportable",
            index=4,
            number=5,
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
    enum_types=[_DRIVEEVENT_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=163,
    serialized_end=409,
)
_DRIVEEVENT.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_DRIVEEVENT.fields_by_name[
    "location"
].message_type = modules_dot_common__msgs_dot_localization__msgs_dot_pose__pb2._POSE
_DRIVEEVENT.fields_by_name["type"].enum_type = _DRIVEEVENT_TYPE
_DRIVEEVENT_TYPE.containing_type = _DRIVEEVENT
DESCRIPTOR.message_types_by_name["DriveEvent"] = _DRIVEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
DriveEvent = _reflection.GeneratedProtocolMessageType(
    "DriveEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _DRIVEEVENT,
        "__module__": "modules.common_msgs.basic_msgs.drive_event_pb2",
    },
)
_sym_db.RegisterMessage(DriveEvent)
