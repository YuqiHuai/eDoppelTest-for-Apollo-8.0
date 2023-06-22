"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common.proto import (
    geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2,
)
from ....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/proto/perception_ultrasonic.proto",
    package="apollo.perception",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n4modules/perception/proto/perception_ultrasonic.proto\x12\x11apollo.perception\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"|\n\x16ImpendingCollisionEdge\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x0ccone_id_list\x18\x02 \x03(\x05B\x02\x18\x01\x12%\n\x05point\x18\x03 \x03(\x0b2\x16.apollo.common.Point3D\x12\x15\n\rtracking_time\x18\x04 \x01(\x01"\x8d\x01\n\x17ImpendingCollisionEdges\x12K\n\x18impending_collision_edge\x18\x01 \x03(\x0b2).apollo.perception.ImpendingCollisionEdge\x12%\n\x06header\x18\x02 \x01(\x0b2\x15.apollo.common.Header',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,
    ],
)
_IMPENDINGCOLLISIONEDGE = _descriptor.Descriptor(
    name="ImpendingCollisionEdge",
    full_name="apollo.perception.ImpendingCollisionEdge",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.perception.ImpendingCollisionEdge.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
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
            name="cone_id_list",
            full_name="apollo.perception.ImpendingCollisionEdge.cone_id_list",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x18\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="point",
            full_name="apollo.perception.ImpendingCollisionEdge.point",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="tracking_time",
            full_name="apollo.perception.ImpendingCollisionEdge.tracking_time",
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
    serialized_end=271,
)
_IMPENDINGCOLLISIONEDGES = _descriptor.Descriptor(
    name="ImpendingCollisionEdges",
    full_name="apollo.perception.ImpendingCollisionEdges",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="impending_collision_edge",
            full_name="apollo.perception.ImpendingCollisionEdges.impending_collision_edge",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.perception.ImpendingCollisionEdges.header",
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
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=274,
    serialized_end=415,
)
_IMPENDINGCOLLISIONEDGE.fields_by_name[
    "point"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_IMPENDINGCOLLISIONEDGES.fields_by_name[
    "impending_collision_edge"
].message_type = _IMPENDINGCOLLISIONEDGE
_IMPENDINGCOLLISIONEDGES.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name["ImpendingCollisionEdge"] = _IMPENDINGCOLLISIONEDGE
DESCRIPTOR.message_types_by_name["ImpendingCollisionEdges"] = _IMPENDINGCOLLISIONEDGES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ImpendingCollisionEdge = _reflection.GeneratedProtocolMessageType(
    "ImpendingCollisionEdge",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPENDINGCOLLISIONEDGE,
        "__module__": "modules.perception.proto.perception_ultrasonic_pb2",
    },
)
_sym_db.RegisterMessage(ImpendingCollisionEdge)
ImpendingCollisionEdges = _reflection.GeneratedProtocolMessageType(
    "ImpendingCollisionEdges",
    (_message.Message,),
    {
        "DESCRIPTOR": _IMPENDINGCOLLISIONEDGES,
        "__module__": "modules.perception.proto.perception_ultrasonic_pb2",
    },
)
_sym_db.RegisterMessage(ImpendingCollisionEdges)
_IMPENDINGCOLLISIONEDGE.fields_by_name["cone_id_list"]._options = None
