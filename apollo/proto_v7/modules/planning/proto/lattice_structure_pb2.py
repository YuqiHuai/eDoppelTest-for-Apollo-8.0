"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/planning/proto/lattice_structure.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n.modules/planning/proto/lattice_structure.proto\x12\x0fapollo.planning"g\n\tStopPoint\x12\t\n\x01s\x18\x01 \x01(\x01\x123\n\x04type\x18\x02 \x01(\x0e2\x1f.apollo.planning.StopPoint.Type:\x04HARD"\x1a\n\x04Type\x12\x08\n\x04HARD\x10\x00\x12\x08\n\x04SOFT\x10\x01"V\n\x0ePlanningTarget\x12.\n\nstop_point\x18\x01 \x01(\x0b2\x1a.apollo.planning.StopPoint\x12\x14\n\x0ccruise_speed\x18\x02 \x01(\x01',
)
_STOPPOINT_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.planning.StopPoint.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="HARD",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SOFT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=144,
    serialized_end=170,
)
_sym_db.RegisterEnumDescriptor(_STOPPOINT_TYPE)
_STOPPOINT = _descriptor.Descriptor(
    name="StopPoint",
    full_name="apollo.planning.StopPoint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="s",
            full_name="apollo.planning.StopPoint.s",
            index=0,
            number=1,
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
            name="type",
            full_name="apollo.planning.StopPoint.type",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=True,
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
    enum_types=[_STOPPOINT_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=67,
    serialized_end=170,
)
_PLANNINGTARGET = _descriptor.Descriptor(
    name="PlanningTarget",
    full_name="apollo.planning.PlanningTarget",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="stop_point",
            full_name="apollo.planning.PlanningTarget.stop_point",
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
            name="cruise_speed",
            full_name="apollo.planning.PlanningTarget.cruise_speed",
            index=1,
            number=2,
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
    serialized_start=172,
    serialized_end=258,
)
_STOPPOINT.fields_by_name["type"].enum_type = _STOPPOINT_TYPE
_STOPPOINT_TYPE.containing_type = _STOPPOINT
_PLANNINGTARGET.fields_by_name["stop_point"].message_type = _STOPPOINT
DESCRIPTOR.message_types_by_name["StopPoint"] = _STOPPOINT
DESCRIPTOR.message_types_by_name["PlanningTarget"] = _PLANNINGTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
StopPoint = _reflection.GeneratedProtocolMessageType(
    "StopPoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _STOPPOINT,
        "__module__": "modules.planning.proto.lattice_structure_pb2",
    },
)
_sym_db.RegisterMessage(StopPoint)
PlanningTarget = _reflection.GeneratedProtocolMessageType(
    "PlanningTarget",
    (_message.Message,),
    {
        "DESCRIPTOR": _PLANNINGTARGET,
        "__module__": "modules.planning.proto.lattice_structure_pb2",
    },
)
_sym_db.RegisterMessage(PlanningTarget)
