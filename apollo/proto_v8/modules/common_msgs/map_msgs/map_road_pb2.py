"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.map_msgs import (
    map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2,
)
from ....modules.common_msgs.map_msgs import (
    map_id_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/map_msgs/map_road.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n+modules/common_msgs/map_msgs/map_road.proto\x12\x0capollo.hdmap\x1a/modules/common_msgs/map_msgs/map_geometry.proto\x1a)modules/common_msgs/map_msgs/map_id.proto"\xa9\x01\n\x0cBoundaryEdge\x12"\n\x05curve\x18\x01 \x01(\x0b2\x13.apollo.hdmap.Curve\x12-\n\x04type\x18\x02 \x01(\x0e2\x1f.apollo.hdmap.BoundaryEdge.Type"F\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x11\n\rLEFT_BOUNDARY\x10\x02\x12\x12\n\x0eRIGHT_BOUNDARY\x10\x03";\n\x0fBoundaryPolygon\x12(\n\x04edge\x18\x01 \x03(\x0b2\x1a.apollo.hdmap.BoundaryEdge"q\n\x0cRoadBoundary\x124\n\router_polygon\x18\x01 \x01(\x0b2\x1d.apollo.hdmap.BoundaryPolygon\x12+\n\x04hole\x18\x02 \x03(\x0b2\x1d.apollo.hdmap.BoundaryPolygon"d\n\x0fRoadROIBoundary\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x123\n\x0froad_boundaries\x18\x02 \x03(\x0b2\x1a.apollo.hdmap.RoadBoundary"|\n\x0bRoadSection\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12!\n\x07lane_id\x18\x02 \x03(\x0b2\x10.apollo.hdmap.Id\x12,\n\x08boundary\x18\x03 \x01(\x0b2\x1a.apollo.hdmap.RoadBoundary"\xd9\x01\n\x04Road\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12*\n\x07section\x18\x02 \x03(\x0b2\x19.apollo.hdmap.RoadSection\x12%\n\x0bjunction_id\x18\x03 \x01(\x0b2\x10.apollo.hdmap.Id\x12%\n\x04type\x18\x04 \x01(\x0e2\x17.apollo.hdmap.Road.Type"9\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07HIGHWAY\x10\x01\x12\r\n\tCITY_ROAD\x10\x02\x12\x08\n\x04PARK\x10\x03',
    dependencies=[
        modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2.DESCRIPTOR,
    ],
)
_BOUNDARYEDGE_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.hdmap.BoundaryEdge.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NORMAL",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LEFT_BOUNDARY",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RIGHT_BOUNDARY",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=253,
    serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_BOUNDARYEDGE_TYPE)
_ROAD_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.hdmap.Road.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HIGHWAY",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CITY_ROAD",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=890,
    serialized_end=947,
)
_sym_db.RegisterEnumDescriptor(_ROAD_TYPE)
_BOUNDARYEDGE = _descriptor.Descriptor(
    name="BoundaryEdge",
    full_name="apollo.hdmap.BoundaryEdge",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="curve",
            full_name="apollo.hdmap.BoundaryEdge.curve",
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
            name="type",
            full_name="apollo.hdmap.BoundaryEdge.type",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_BOUNDARYEDGE_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=154,
    serialized_end=323,
)
_BOUNDARYPOLYGON = _descriptor.Descriptor(
    name="BoundaryPolygon",
    full_name="apollo.hdmap.BoundaryPolygon",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="edge",
            full_name="apollo.hdmap.BoundaryPolygon.edge",
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
    serialized_start=325,
    serialized_end=384,
)
_ROADBOUNDARY = _descriptor.Descriptor(
    name="RoadBoundary",
    full_name="apollo.hdmap.RoadBoundary",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="outer_polygon",
            full_name="apollo.hdmap.RoadBoundary.outer_polygon",
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
            name="hole",
            full_name="apollo.hdmap.RoadBoundary.hole",
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
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=386,
    serialized_end=499,
)
_ROADROIBOUNDARY = _descriptor.Descriptor(
    name="RoadROIBoundary",
    full_name="apollo.hdmap.RoadROIBoundary",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.RoadROIBoundary.id",
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
            name="road_boundaries",
            full_name="apollo.hdmap.RoadROIBoundary.road_boundaries",
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
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=501,
    serialized_end=601,
)
_ROADSECTION = _descriptor.Descriptor(
    name="RoadSection",
    full_name="apollo.hdmap.RoadSection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.RoadSection.id",
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
            name="lane_id",
            full_name="apollo.hdmap.RoadSection.lane_id",
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
        _descriptor.FieldDescriptor(
            name="boundary",
            full_name="apollo.hdmap.RoadSection.boundary",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=603,
    serialized_end=727,
)
_ROAD = _descriptor.Descriptor(
    name="Road",
    full_name="apollo.hdmap.Road",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.Road.id",
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
            name="section",
            full_name="apollo.hdmap.Road.section",
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
        _descriptor.FieldDescriptor(
            name="junction_id",
            full_name="apollo.hdmap.Road.junction_id",
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
            full_name="apollo.hdmap.Road.type",
            index=3,
            number=4,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_ROAD_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=730,
    serialized_end=947,
)
_BOUNDARYEDGE.fields_by_name[
    "curve"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2._CURVE
_BOUNDARYEDGE.fields_by_name["type"].enum_type = _BOUNDARYEDGE_TYPE
_BOUNDARYEDGE_TYPE.containing_type = _BOUNDARYEDGE
_BOUNDARYPOLYGON.fields_by_name["edge"].message_type = _BOUNDARYEDGE
_ROADBOUNDARY.fields_by_name["outer_polygon"].message_type = _BOUNDARYPOLYGON
_ROADBOUNDARY.fields_by_name["hole"].message_type = _BOUNDARYPOLYGON
_ROADROIBOUNDARY.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_ROADROIBOUNDARY.fields_by_name["road_boundaries"].message_type = _ROADBOUNDARY
_ROADSECTION.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_ROADSECTION.fields_by_name[
    "lane_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_ROADSECTION.fields_by_name["boundary"].message_type = _ROADBOUNDARY
_ROAD.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_ROAD.fields_by_name["section"].message_type = _ROADSECTION
_ROAD.fields_by_name[
    "junction_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_ROAD.fields_by_name["type"].enum_type = _ROAD_TYPE
_ROAD_TYPE.containing_type = _ROAD
DESCRIPTOR.message_types_by_name["BoundaryEdge"] = _BOUNDARYEDGE
DESCRIPTOR.message_types_by_name["BoundaryPolygon"] = _BOUNDARYPOLYGON
DESCRIPTOR.message_types_by_name["RoadBoundary"] = _ROADBOUNDARY
DESCRIPTOR.message_types_by_name["RoadROIBoundary"] = _ROADROIBOUNDARY
DESCRIPTOR.message_types_by_name["RoadSection"] = _ROADSECTION
DESCRIPTOR.message_types_by_name["Road"] = _ROAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
BoundaryEdge = _reflection.GeneratedProtocolMessageType(
    "BoundaryEdge",
    (_message.Message,),
    {
        "DESCRIPTOR": _BOUNDARYEDGE,
        "__module__": "modules.common_msgs.map_msgs.map_road_pb2",
    },
)
_sym_db.RegisterMessage(BoundaryEdge)
BoundaryPolygon = _reflection.GeneratedProtocolMessageType(
    "BoundaryPolygon",
    (_message.Message,),
    {
        "DESCRIPTOR": _BOUNDARYPOLYGON,
        "__module__": "modules.common_msgs.map_msgs.map_road_pb2",
    },
)
_sym_db.RegisterMessage(BoundaryPolygon)
RoadBoundary = _reflection.GeneratedProtocolMessageType(
    "RoadBoundary",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROADBOUNDARY,
        "__module__": "modules.common_msgs.map_msgs.map_road_pb2",
    },
)
_sym_db.RegisterMessage(RoadBoundary)
RoadROIBoundary = _reflection.GeneratedProtocolMessageType(
    "RoadROIBoundary",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROADROIBOUNDARY,
        "__module__": "modules.common_msgs.map_msgs.map_road_pb2",
    },
)
_sym_db.RegisterMessage(RoadROIBoundary)
RoadSection = _reflection.GeneratedProtocolMessageType(
    "RoadSection",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROADSECTION,
        "__module__": "modules.common_msgs.map_msgs.map_road_pb2",
    },
)
_sym_db.RegisterMessage(RoadSection)
Road = _reflection.GeneratedProtocolMessageType(
    "Road",
    (_message.Message,),
    {"DESCRIPTOR": _ROAD, "__module__": "modules.common_msgs.map_msgs.map_road_pb2"},
)
_sym_db.RegisterMessage(Road)
