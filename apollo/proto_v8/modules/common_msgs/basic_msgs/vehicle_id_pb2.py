"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/basic_msgs/vehicle_id.proto",
    package="apollo.common",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/modules/common_msgs/basic_msgs/vehicle_id.proto\x12\rapollo.common"@\n\tVehicleID\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\r\n\x05plate\x18\x02 \x01(\t\x12\x17\n\x0fother_unique_id\x18\x03 \x01(\t',
)
_VEHICLEID = _descriptor.Descriptor(
    name="VehicleID",
    full_name="apollo.common.VehicleID",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="vin",
            full_name="apollo.common.VehicleID.vin",
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
            name="plate",
            full_name="apollo.common.VehicleID.plate",
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
        _descriptor.FieldDescriptor(
            name="other_unique_id",
            full_name="apollo.common.VehicleID.other_unique_id",
            index=2,
            number=3,
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=66,
    serialized_end=130,
)
DESCRIPTOR.message_types_by_name["VehicleID"] = _VEHICLEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
VehicleID = _reflection.GeneratedProtocolMessageType(
    "VehicleID",
    (_message.Message,),
    {
        "DESCRIPTOR": _VEHICLEID,
        "__module__": "modules.common_msgs.basic_msgs.vehicle_id_pb2",
    },
)
_sym_db.RegisterMessage(VehicleID)
