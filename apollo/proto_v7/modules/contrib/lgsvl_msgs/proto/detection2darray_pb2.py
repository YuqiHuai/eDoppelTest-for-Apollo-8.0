"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from .....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from .....modules.contrib.lgsvl_msgs.proto import (
    detection2d_pb2 as modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/contrib/lgsvl_msgs/proto/detection2darray.proto",
    package="apollo.contrib.lgsvl_msgs",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n7modules/contrib/lgsvl_msgs/proto/detection2darray.proto\x12\x19apollo.contrib.lgsvl_msgs\x1a!modules/common/proto/header.proto\x1a2modules/contrib/lgsvl_msgs/proto/detection2d.proto"u\n\x10Detection2DArray\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12:\n\ndetections\x18\x02 \x03(\x0b2&.apollo.contrib.lgsvl_msgs.Detection2Db\x06proto3',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2.DESCRIPTOR,
    ],
)
_DETECTION2DARRAY = _descriptor.Descriptor(
    name="Detection2DArray",
    full_name="apollo.contrib.lgsvl_msgs.Detection2DArray",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.contrib.lgsvl_msgs.Detection2DArray.header",
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
            name="detections",
            full_name="apollo.contrib.lgsvl_msgs.Detection2DArray.detections",
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
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=173,
    serialized_end=290,
)
_DETECTION2DARRAY.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_DETECTION2DARRAY.fields_by_name[
    "detections"
].message_type = (
    modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2._DETECTION2D
)
DESCRIPTOR.message_types_by_name["Detection2DArray"] = _DETECTION2DARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Detection2DArray = _reflection.GeneratedProtocolMessageType(
    "Detection2DArray",
    (_message.Message,),
    {
        "DESCRIPTOR": _DETECTION2DARRAY,
        "__module__": "modules.contrib.lgsvl_msgs.proto.detection2darray_pb2",
    },
)
_sym_db.RegisterMessage(Detection2DArray)
