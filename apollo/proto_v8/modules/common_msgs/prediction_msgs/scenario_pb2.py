"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/prediction_msgs/scenario.proto",
    package="apollo.prediction",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2modules/common_msgs/prediction_msgs/scenario.proto\x12\x11apollo.prediction"\xe8\x01\n\x08Scenario\x127\n\x04type\x18\x01 \x01(\x0e2 .apollo.prediction.Scenario.Type:\x07UNKNOWN\x12\x13\n\x0bjunction_id\x18\x02 \x01(\t"\x8d\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x06CRUISE\x10\xe8\x07\x12\x11\n\x0cCRUISE_URBAN\x10\xe9\x07\x12\x13\n\x0eCRUISE_HIGHWAY\x10\xea\x07\x12\r\n\x08JUNCTION\x10\xd0\x0f\x12\x1b\n\x16JUNCTION_TRAFFIC_LIGHT\x10\xd1\x0f\x12\x17\n\x12JUNCTION_STOP_SIGN\x10\xd2\x0f',
)
_SCENARIO_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.prediction.Scenario.Type",
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
            name="CRUISE",
            index=1,
            number=1000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CRUISE_URBAN",
            index=2,
            number=1001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CRUISE_HIGHWAY",
            index=3,
            number=1002,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="JUNCTION",
            index=4,
            number=2000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="JUNCTION_TRAFFIC_LIGHT",
            index=5,
            number=2001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="JUNCTION_STOP_SIGN",
            index=6,
            number=2002,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=165,
    serialized_end=306,
)
_sym_db.RegisterEnumDescriptor(_SCENARIO_TYPE)
_SCENARIO = _descriptor.Descriptor(
    name="Scenario",
    full_name="apollo.prediction.Scenario",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="apollo.prediction.Scenario.type",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="junction_id",
            full_name="apollo.prediction.Scenario.junction_id",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SCENARIO_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=306,
)
_SCENARIO.fields_by_name["type"].enum_type = _SCENARIO_TYPE
_SCENARIO_TYPE.containing_type = _SCENARIO
DESCRIPTOR.message_types_by_name["Scenario"] = _SCENARIO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Scenario = _reflection.GeneratedProtocolMessageType(
    "Scenario",
    (_message.Message,),
    {
        "DESCRIPTOR": _SCENARIO,
        "__module__": "modules.common_msgs.prediction_msgs.scenario_pb2",
    },
)
_sym_db.RegisterMessage(Scenario)
