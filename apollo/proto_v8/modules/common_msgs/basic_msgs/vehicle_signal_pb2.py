"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/basic_msgs/vehicle_signal.proto",
    package="apollo.common",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n3modules/common_msgs/basic_msgs/vehicle_signal.proto\x12\rapollo.common"\xee\x01\n\rVehicleSignal\x12<\n\x0bturn_signal\x18\x01 \x01(\x0e2\'.apollo.common.VehicleSignal.TurnSignal\x12\x11\n\thigh_beam\x18\x02 \x01(\x08\x12\x10\n\x08low_beam\x18\x03 \x01(\x08\x12\x0c\n\x04horn\x18\x04 \x01(\x08\x12\x17\n\x0femergency_light\x18\x05 \x01(\x08"S\n\nTurnSignal\x12\r\n\tTURN_NONE\x10\x00\x12\r\n\tTURN_LEFT\x10\x01\x12\x0e\n\nTURN_RIGHT\x10\x02\x12\x17\n\x13TURN_HAZARD_WARNING\x10\x03',
)
_VEHICLESIGNAL_TURNSIGNAL = _descriptor.EnumDescriptor(
    name="TurnSignal",
    full_name="apollo.common.VehicleSignal.TurnSignal",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="TURN_NONE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TURN_LEFT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TURN_RIGHT",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TURN_HAZARD_WARNING",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=226,
    serialized_end=309,
)
_sym_db.RegisterEnumDescriptor(_VEHICLESIGNAL_TURNSIGNAL)
_VEHICLESIGNAL = _descriptor.Descriptor(
    name="VehicleSignal",
    full_name="apollo.common.VehicleSignal",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="turn_signal",
            full_name="apollo.common.VehicleSignal.turn_signal",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="high_beam",
            full_name="apollo.common.VehicleSignal.high_beam",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="low_beam",
            full_name="apollo.common.VehicleSignal.low_beam",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="horn",
            full_name="apollo.common.VehicleSignal.horn",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="emergency_light",
            full_name="apollo.common.VehicleSignal.emergency_light",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    enum_types=[_VEHICLESIGNAL_TURNSIGNAL],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=71,
    serialized_end=309,
)
_VEHICLESIGNAL.fields_by_name["turn_signal"].enum_type = _VEHICLESIGNAL_TURNSIGNAL
_VEHICLESIGNAL_TURNSIGNAL.containing_type = _VEHICLESIGNAL
DESCRIPTOR.message_types_by_name["VehicleSignal"] = _VEHICLESIGNAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
VehicleSignal = _reflection.GeneratedProtocolMessageType(
    "VehicleSignal",
    (_message.Message,),
    {
        "DESCRIPTOR": _VEHICLESIGNAL,
        "__module__": "modules.common_msgs.basic_msgs.vehicle_signal_pb2",
    },
)
_sym_db.RegisterMessage(VehicleSignal)
