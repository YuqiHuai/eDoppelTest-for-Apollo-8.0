"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/map/proto/map_id.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1emodules/map/proto/map_id.proto\x12\x0capollo.hdmap"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\t',
)
_ID = _descriptor.Descriptor(
    name="Id",
    full_name="apollo.hdmap.Id",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.Id.id",
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
    serialized_start=48,
    serialized_end=64,
)
DESCRIPTOR.message_types_by_name["Id"] = _ID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Id = _reflection.GeneratedProtocolMessageType(
    "Id",
    (_message.Message,),
    {"DESCRIPTOR": _ID, "__module__": "modules.map.proto.map_id_pb2"},
)
_sym_db.RegisterMessage(Id)
