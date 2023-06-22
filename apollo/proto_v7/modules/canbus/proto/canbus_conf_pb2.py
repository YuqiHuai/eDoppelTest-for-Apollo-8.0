"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.canbus.proto import (
    vehicle_parameter_pb2 as modules_dot_canbus_dot_proto_dot_vehicle__parameter__pb2,
)
from ....modules.drivers.canbus.proto import (
    can_card_parameter_pb2 as modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/canbus/proto/canbus_conf.proto",
    package="apollo.canbus",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n&modules/canbus/proto/canbus_conf.proto\x12\rapollo.canbus\x1a5modules/drivers/canbus/proto/can_card_parameter.proto\x1a,modules/canbus/proto/vehicle_parameter.proto"\xf5\x01\n\nCanbusConf\x12:\n\x11vehicle_parameter\x18\x01 \x01(\x0b2\x1f.apollo.canbus.VehicleParameter\x12C\n\x12can_card_parameter\x18\x02 \x01(\x0b2\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11enable_debug_mode\x18\x03 \x01(\x08:\x05false\x12"\n\x13enable_receiver_log\x18\x04 \x01(\x08:\x05false\x12 \n\x11enable_sender_log\x18\x05 \x01(\x08:\x05false',
    dependencies=[
        modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2.DESCRIPTOR,
        modules_dot_canbus_dot_proto_dot_vehicle__parameter__pb2.DESCRIPTOR,
    ],
)
_CANBUSCONF = _descriptor.Descriptor(
    name="CanbusConf",
    full_name="apollo.canbus.CanbusConf",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="vehicle_parameter",
            full_name="apollo.canbus.CanbusConf.vehicle_parameter",
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
            name="can_card_parameter",
            full_name="apollo.canbus.CanbusConf.can_card_parameter",
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
            name="enable_debug_mode",
            full_name="apollo.canbus.CanbusConf.enable_debug_mode",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
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
            name="enable_receiver_log",
            full_name="apollo.canbus.CanbusConf.enable_receiver_log",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
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
            name="enable_sender_log",
            full_name="apollo.canbus.CanbusConf.enable_sender_log",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=159,
    serialized_end=404,
)
_CANBUSCONF.fields_by_name[
    "vehicle_parameter"
].message_type = (
    modules_dot_canbus_dot_proto_dot_vehicle__parameter__pb2._VEHICLEPARAMETER
)
_CANBUSCONF.fields_by_name[
    "can_card_parameter"
].message_type = (
    modules_dot_drivers_dot_canbus_dot_proto_dot_can__card__parameter__pb2._CANCARDPARAMETER
)
DESCRIPTOR.message_types_by_name["CanbusConf"] = _CANBUSCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CanbusConf = _reflection.GeneratedProtocolMessageType(
    "CanbusConf",
    (_message.Message,),
    {"DESCRIPTOR": _CANBUSCONF, "__module__": "modules.canbus.proto.canbus_conf_pb2"},
)
_sym_db.RegisterMessage(CanbusConf)
