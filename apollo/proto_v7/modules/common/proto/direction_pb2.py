"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common/proto/direction.proto",
    package="apollo.common",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n$modules/common/proto/direction.proto\x12\rapollo.common*q\n\tDirection\x12\x08\n\x04EAST\x10\x00\x12\x08\n\x04WEST\x10\x01\x12\t\n\x05SOUTH\x10\x02\x12\t\n\x05NORTH\x10\x03\x12\r\n\tNORTHEAST\x10\x04\x12\r\n\tSOUTHEAST\x10\x05\x12\r\n\tSOUTHWEST\x10\x06\x12\r\n\tNORTHWEST\x10\x07",
)
_DIRECTION = _descriptor.EnumDescriptor(
    name="Direction",
    full_name="apollo.common.Direction",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="EAST",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WEST",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SOUTH",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NORTH",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NORTHEAST",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SOUTHEAST",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SOUTHWEST",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NORTHWEST",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=55,
    serialized_end=168,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)
Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
EAST = 0
WEST = 1
SOUTH = 2
NORTH = 3
NORTHEAST = 4
SOUTHEAST = 5
SOUTHWEST = 6
NORTHWEST = 7
DESCRIPTOR.enum_types_by_name["Direction"] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
