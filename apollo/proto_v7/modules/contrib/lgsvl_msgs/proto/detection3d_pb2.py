"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from .....modules.common.proto import (
    geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2,
)
from .....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)
from .....modules.contrib.lgsvl_msgs.proto import (
    detection2d_pb2 as modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/contrib/lgsvl_msgs/proto/detection3d.proto",
    package="apollo.contrib.lgsvl_msgs",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2modules/contrib/lgsvl_msgs/proto/detection3d.proto\x12\x19apollo.contrib.lgsvl_msgs\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\x1a2modules/contrib/lgsvl_msgs/proto/detection2d.proto"`\n\x04Pose\x12(\n\x08position\x18\x01 \x01(\x0b2\x16.apollo.common.Point3D\x12.\n\x0borientation\x18\x02 \x01(\x0b2\x19.apollo.common.Quaternion"t\n\rBoundingBox3D\x121\n\x08position\x18\x01 \x01(\x0b2\x1f.apollo.contrib.lgsvl_msgs.Pose\x120\n\x04size\x18\x02 \x01(\x0b2".apollo.contrib.lgsvl_msgs.Vector3"\xca\x01\n\x0bDetection3D\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05label\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x01\x126\n\x04bbox\x18\x05 \x01(\x0b2(.apollo.contrib.lgsvl_msgs.BoundingBox3D\x122\n\x08velocity\x18\x06 \x01(\x0b2 .apollo.contrib.lgsvl_msgs.Twistb\x06proto3',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,
        modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2.DESCRIPTOR,
    ],
)
_POSE = _descriptor.Descriptor(
    name="Pose",
    full_name="apollo.contrib.lgsvl_msgs.Pose",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="position",
            full_name="apollo.contrib.lgsvl_msgs.Pose.position",
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
            name="orientation",
            full_name="apollo.contrib.lgsvl_msgs.Pose.orientation",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=205,
    serialized_end=301,
)
_BOUNDINGBOX3D = _descriptor.Descriptor(
    name="BoundingBox3D",
    full_name="apollo.contrib.lgsvl_msgs.BoundingBox3D",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="position",
            full_name="apollo.contrib.lgsvl_msgs.BoundingBox3D.position",
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
            name="size",
            full_name="apollo.contrib.lgsvl_msgs.BoundingBox3D.size",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=303,
    serialized_end=419,
)
_DETECTION3D = _descriptor.Descriptor(
    name="Detection3D",
    full_name="apollo.contrib.lgsvl_msgs.Detection3D",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.contrib.lgsvl_msgs.Detection3D.header",
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
            name="id",
            full_name="apollo.contrib.lgsvl_msgs.Detection3D.id",
            index=1,
            number=2,
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
            name="label",
            full_name="apollo.contrib.lgsvl_msgs.Detection3D.label",
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
            name="score",
            full_name="apollo.contrib.lgsvl_msgs.Detection3D.score",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="bbox",
            full_name="apollo.contrib.lgsvl_msgs.Detection3D.bbox",
            index=4,
            number=5,
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
            name="velocity",
            full_name="apollo.contrib.lgsvl_msgs.Detection3D.velocity",
            index=5,
            number=6,
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
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=422,
    serialized_end=624,
)
_POSE.fields_by_name[
    "position"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_POSE.fields_by_name[
    "orientation"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._QUATERNION
_BOUNDINGBOX3D.fields_by_name["position"].message_type = _POSE
_BOUNDINGBOX3D.fields_by_name[
    "size"
].message_type = (
    modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2._VECTOR3
)
_DETECTION3D.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_DETECTION3D.fields_by_name["bbox"].message_type = _BOUNDINGBOX3D
_DETECTION3D.fields_by_name[
    "velocity"
].message_type = (
    modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2._TWIST
)
DESCRIPTOR.message_types_by_name["Pose"] = _POSE
DESCRIPTOR.message_types_by_name["BoundingBox3D"] = _BOUNDINGBOX3D
DESCRIPTOR.message_types_by_name["Detection3D"] = _DETECTION3D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Pose = _reflection.GeneratedProtocolMessageType(
    "Pose",
    (_message.Message,),
    {
        "DESCRIPTOR": _POSE,
        "__module__": "modules.contrib.lgsvl_msgs.proto.detection3d_pb2",
    },
)
_sym_db.RegisterMessage(Pose)
BoundingBox3D = _reflection.GeneratedProtocolMessageType(
    "BoundingBox3D",
    (_message.Message,),
    {
        "DESCRIPTOR": _BOUNDINGBOX3D,
        "__module__": "modules.contrib.lgsvl_msgs.proto.detection3d_pb2",
    },
)
_sym_db.RegisterMessage(BoundingBox3D)
Detection3D = _reflection.GeneratedProtocolMessageType(
    "Detection3D",
    (_message.Message,),
    {
        "DESCRIPTOR": _DETECTION3D,
        "__module__": "modules.contrib.lgsvl_msgs.proto.detection3d_pb2",
    },
)
_sym_db.RegisterMessage(Detection3D)
