"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import (
    chassis_pb2 as modules_dot_canbus_dot_proto_dot_chassis__pb2,
)
from ....modules.common.configs.proto import (
    vehicle_config_pb2 as modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/canbus/proto/vehicle_parameter.proto",
    package="apollo.canbus",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n,modules/canbus/proto/vehicle_parameter.proto\x12\rapollo.canbus\x1a"modules/canbus/proto/chassis.proto\x1a1modules/common/configs/proto/vehicle_config.proto"\xb3\x01\n\x10VehicleParameter\x12*\n\x05brand\x18\x01 \x01(\x0e2\x1b.apollo.common.VehicleBrand\x12\x18\n\x10max_engine_pedal\x18\x02 \x01(\x01\x12\x1f\n\x17max_enable_fail_attempt\x18\x03 \x01(\x05\x128\n\x0cdriving_mode\x18\x04 \x01(\x0e2".apollo.canbus.Chassis.DrivingMode',
    dependencies=[
        modules_dot_canbus_dot_proto_dot_chassis__pb2.DESCRIPTOR,
        modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2.DESCRIPTOR,
    ],
)
_VEHICLEPARAMETER = _descriptor.Descriptor(
    name="VehicleParameter",
    full_name="apollo.canbus.VehicleParameter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="brand",
            full_name="apollo.canbus.VehicleParameter.brand",
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
            name="max_engine_pedal",
            full_name="apollo.canbus.VehicleParameter.max_engine_pedal",
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
        _descriptor.FieldDescriptor(
            name="max_enable_fail_attempt",
            full_name="apollo.canbus.VehicleParameter.max_enable_fail_attempt",
            index=2,
            number=3,
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
            name="driving_mode",
            full_name="apollo.canbus.VehicleParameter.driving_mode",
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=151,
    serialized_end=330,
)
_VEHICLEPARAMETER.fields_by_name[
    "brand"
].enum_type = (
    modules_dot_common_dot_configs_dot_proto_dot_vehicle__config__pb2._VEHICLEBRAND
)
_VEHICLEPARAMETER.fields_by_name[
    "driving_mode"
].enum_type = modules_dot_canbus_dot_proto_dot_chassis__pb2._CHASSIS_DRIVINGMODE
DESCRIPTOR.message_types_by_name["VehicleParameter"] = _VEHICLEPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
VehicleParameter = _reflection.GeneratedProtocolMessageType(
    "VehicleParameter",
    (_message.Message,),
    {
        "DESCRIPTOR": _VEHICLEPARAMETER,
        "__module__": "modules.canbus.proto.vehicle_parameter_pb2",
    },
)
_sym_db.RegisterMessage(VehicleParameter)
