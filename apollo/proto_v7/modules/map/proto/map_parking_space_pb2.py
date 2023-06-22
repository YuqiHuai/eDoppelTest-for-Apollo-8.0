"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.map.proto import (
    map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2,
)
from ....modules.map.proto import (
    map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/map/proto/map_parking_space.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n)modules/map/proto/map_parking_space.proto\x12\x0capollo.hdmap\x1a$modules/map/proto/map_geometry.proto\x1a\x1emodules/map/proto/map_id.proto"\x8b\x01\n\x0cParkingSpace\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id\x12\x0f\n\x07heading\x18\x04 \x01(\x01"x\n\nParkingLot\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id',
    dependencies=[
        modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR,
        modules_dot_map_dot_proto_dot_map__id__pb2.DESCRIPTOR,
    ],
)
_PARKINGSPACE = _descriptor.Descriptor(
    name="ParkingSpace",
    full_name="apollo.hdmap.ParkingSpace",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.ParkingSpace.id",
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
            name="polygon",
            full_name="apollo.hdmap.ParkingSpace.polygon",
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
            name="overlap_id",
            full_name="apollo.hdmap.ParkingSpace.overlap_id",
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
            name="heading",
            full_name="apollo.hdmap.ParkingSpace.heading",
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
    serialized_start=130,
    serialized_end=269,
)
_PARKINGLOT = _descriptor.Descriptor(
    name="ParkingLot",
    full_name="apollo.hdmap.ParkingLot",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.ParkingLot.id",
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
            name="polygon",
            full_name="apollo.hdmap.ParkingLot.polygon",
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
            name="overlap_id",
            full_name="apollo.hdmap.ParkingLot.overlap_id",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=271,
    serialized_end=391,
)
_PARKINGSPACE.fields_by_name[
    "id"
].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_PARKINGSPACE.fields_by_name[
    "polygon"
].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._POLYGON
_PARKINGSPACE.fields_by_name[
    "overlap_id"
].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_PARKINGLOT.fields_by_name[
    "id"
].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_PARKINGLOT.fields_by_name[
    "polygon"
].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._POLYGON
_PARKINGLOT.fields_by_name[
    "overlap_id"
].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
DESCRIPTOR.message_types_by_name["ParkingSpace"] = _PARKINGSPACE
DESCRIPTOR.message_types_by_name["ParkingLot"] = _PARKINGLOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ParkingSpace = _reflection.GeneratedProtocolMessageType(
    "ParkingSpace",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARKINGSPACE,
        "__module__": "modules.map.proto.map_parking_space_pb2",
    },
)
_sym_db.RegisterMessage(ParkingSpace)
ParkingLot = _reflection.GeneratedProtocolMessageType(
    "ParkingLot",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARKINGLOT,
        "__module__": "modules.map.proto.map_parking_space_pb2",
    },
)
_sym_db.RegisterMessage(ParkingLot)
