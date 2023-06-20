"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/map_msgs/map_geometry.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/modules/common_msgs/map_msgs/map_geometry.proto\x12\x0capollo.hdmap\x1a-modules/common_msgs/basic_msgs/geometry.proto"1\n\x07Polygon\x12&\n\x05point\x18\x01 \x03(\x0b2\x17.apollo.common.PointENU"5\n\x0bLineSegment\x12&\n\x05point\x18\x01 \x03(\x0b2\x17.apollo.common.PointENU"\xac\x01\n\x0cCurveSegment\x121\n\x0cline_segment\x18\x01 \x01(\x0b2\x19.apollo.hdmap.LineSegmentH\x00\x12\t\n\x01s\x18\x06 \x01(\x01\x12/\n\x0estart_position\x18\x07 \x01(\x0b2\x17.apollo.common.PointENU\x12\x0f\n\x07heading\x18\x08 \x01(\x01\x12\x0e\n\x06length\x18\t \x01(\x01B\x0c\n\ncurve_type"4\n\x05Curve\x12+\n\x07segment\x18\x01 \x03(\x0b2\x1a.apollo.hdmap.CurveSegment',
    dependencies=[
        modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2.DESCRIPTOR
    ],
)
_POLYGON = _descriptor.Descriptor(
    name="Polygon",
    full_name="apollo.hdmap.Polygon",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="point",
            full_name="apollo.hdmap.Polygon.point",
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
    serialized_start=112,
    serialized_end=161,
)
_LINESEGMENT = _descriptor.Descriptor(
    name="LineSegment",
    full_name="apollo.hdmap.LineSegment",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="point",
            full_name="apollo.hdmap.LineSegment.point",
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
    serialized_start=163,
    serialized_end=216,
)
_CURVESEGMENT = _descriptor.Descriptor(
    name="CurveSegment",
    full_name="apollo.hdmap.CurveSegment",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="line_segment",
            full_name="apollo.hdmap.CurveSegment.line_segment",
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
            name="s",
            full_name="apollo.hdmap.CurveSegment.s",
            index=1,
            number=6,
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
            name="start_position",
            full_name="apollo.hdmap.CurveSegment.start_position",
            index=2,
            number=7,
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
            name="heading",
            full_name="apollo.hdmap.CurveSegment.heading",
            index=3,
            number=8,
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
            name="length",
            full_name="apollo.hdmap.CurveSegment.length",
            index=4,
            number=9,
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
    oneofs=[
        _descriptor.OneofDescriptor(
            name="curve_type",
            full_name="apollo.hdmap.CurveSegment.curve_type",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=219,
    serialized_end=391,
)
_CURVE = _descriptor.Descriptor(
    name="Curve",
    full_name="apollo.hdmap.Curve",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="segment",
            full_name="apollo.hdmap.Curve.segment",
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
    serialized_start=393,
    serialized_end=445,
)
_POLYGON.fields_by_name[
    "point"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2._POINTENU
_LINESEGMENT.fields_by_name[
    "point"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2._POINTENU
_CURVESEGMENT.fields_by_name["line_segment"].message_type = _LINESEGMENT
_CURVESEGMENT.fields_by_name[
    "start_position"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2._POINTENU
_CURVESEGMENT.oneofs_by_name["curve_type"].fields.append(
    _CURVESEGMENT.fields_by_name["line_segment"]
)
_CURVESEGMENT.fields_by_name[
    "line_segment"
].containing_oneof = _CURVESEGMENT.oneofs_by_name["curve_type"]
_CURVE.fields_by_name["segment"].message_type = _CURVESEGMENT
DESCRIPTOR.message_types_by_name["Polygon"] = _POLYGON
DESCRIPTOR.message_types_by_name["LineSegment"] = _LINESEGMENT
DESCRIPTOR.message_types_by_name["CurveSegment"] = _CURVESEGMENT
DESCRIPTOR.message_types_by_name["Curve"] = _CURVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Polygon = _reflection.GeneratedProtocolMessageType(
    "Polygon",
    (_message.Message,),
    {
        "DESCRIPTOR": _POLYGON,
        "__module__": "modules.common_msgs.map_msgs.map_geometry_pb2",
    },
)
_sym_db.RegisterMessage(Polygon)
LineSegment = _reflection.GeneratedProtocolMessageType(
    "LineSegment",
    (_message.Message,),
    {
        "DESCRIPTOR": _LINESEGMENT,
        "__module__": "modules.common_msgs.map_msgs.map_geometry_pb2",
    },
)
_sym_db.RegisterMessage(LineSegment)
CurveSegment = _reflection.GeneratedProtocolMessageType(
    "CurveSegment",
    (_message.Message,),
    {
        "DESCRIPTOR": _CURVESEGMENT,
        "__module__": "modules.common_msgs.map_msgs.map_geometry_pb2",
    },
)
_sym_db.RegisterMessage(CurveSegment)
Curve = _reflection.GeneratedProtocolMessageType(
    "Curve",
    (_message.Message,),
    {
        "DESCRIPTOR": _CURVE,
        "__module__": "modules.common_msgs.map_msgs.map_geometry_pb2",
    },
)
_sym_db.RegisterMessage(Curve)
