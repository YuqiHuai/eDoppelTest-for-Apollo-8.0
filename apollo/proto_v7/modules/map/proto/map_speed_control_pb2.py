"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.map.proto import (
    map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/map/proto/map_speed_control.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n)modules/map/proto/map_speed_control.proto\x12\x0capollo.hdmap\x1a$modules/map/proto/map_geometry.proto"Y\n\x0cSpeedControl\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12\x13\n\x0bspeed_limit\x18\x03 \x01(\x01"B\n\rSpeedControls\x121\n\rspeed_control\x18\x01 \x03(\x0b2\x1a.apollo.hdmap.SpeedControl',
    dependencies=[modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR],
)
_SPEEDCONTROL = _descriptor.Descriptor(
    name="SpeedControl",
    full_name="apollo.hdmap.SpeedControl",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="apollo.hdmap.SpeedControl.name",
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
            name="polygon",
            full_name="apollo.hdmap.SpeedControl.polygon",
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
            name="speed_limit",
            full_name="apollo.hdmap.SpeedControl.speed_limit",
            index=2,
            number=3,
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
    serialized_start=97,
    serialized_end=186,
)
_SPEEDCONTROLS = _descriptor.Descriptor(
    name="SpeedControls",
    full_name="apollo.hdmap.SpeedControls",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="speed_control",
            full_name="apollo.hdmap.SpeedControls.speed_control",
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
    serialized_start=188,
    serialized_end=254,
)
_SPEEDCONTROL.fields_by_name[
    "polygon"
].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._POLYGON
_SPEEDCONTROLS.fields_by_name["speed_control"].message_type = _SPEEDCONTROL
DESCRIPTOR.message_types_by_name["SpeedControl"] = _SPEEDCONTROL
DESCRIPTOR.message_types_by_name["SpeedControls"] = _SPEEDCONTROLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SpeedControl = _reflection.GeneratedProtocolMessageType(
    "SpeedControl",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPEEDCONTROL,
        "__module__": "modules.map.proto.map_speed_control_pb2",
    },
)
_sym_db.RegisterMessage(SpeedControl)
SpeedControls = _reflection.GeneratedProtocolMessageType(
    "SpeedControls",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPEEDCONTROLS,
        "__module__": "modules.map.proto.map_speed_control_pb2",
    },
)
_sym_db.RegisterMessage(SpeedControls)
