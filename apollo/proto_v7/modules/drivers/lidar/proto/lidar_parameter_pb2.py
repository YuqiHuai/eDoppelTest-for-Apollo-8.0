"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/drivers/lidar/proto/lidar_parameter.proto",
    package="apollo.drivers.lidar",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n1modules/drivers/lidar/proto/lidar_parameter.proto\x12\x14apollo.drivers.lidar"\xeb\x01\n\x0eLidarParameter\x12>\n\x05brand\x18\x01 \x02(\x0e2/.apollo.drivers.lidar.LidarParameter.LidarBrand"4\n\nLidarBrand\x12\x0c\n\x08VELODYNE\x10\x00\x12\t\n\x05HESAI\x10\x01\x12\r\n\tROBOSENSE\x10\x02"c\n\x0eLidarChannelId\x12\x13\n\x0fCHANNEL_ID_ZERO\x10\x00\x12\x12\n\x0eCHANNEL_ID_ONE\x10\x01\x12\x12\n\x0eCHANNEL_ID_TWO\x10\x02\x12\x14\n\x10CHANNEL_ID_THREE\x10\x03',
)
_LIDARPARAMETER_LIDARBRAND = _descriptor.EnumDescriptor(
    name="LidarBrand",
    full_name="apollo.drivers.lidar.LidarParameter.LidarBrand",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="VELODYNE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HESAI",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROBOSENSE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=158,
    serialized_end=210,
)
_sym_db.RegisterEnumDescriptor(_LIDARPARAMETER_LIDARBRAND)
_LIDARPARAMETER_LIDARCHANNELID = _descriptor.EnumDescriptor(
    name="LidarChannelId",
    full_name="apollo.drivers.lidar.LidarParameter.LidarChannelId",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CHANNEL_ID_ZERO",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANNEL_ID_ONE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANNEL_ID_TWO",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANNEL_ID_THREE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=212,
    serialized_end=311,
)
_sym_db.RegisterEnumDescriptor(_LIDARPARAMETER_LIDARCHANNELID)
_LIDARPARAMETER = _descriptor.Descriptor(
    name="LidarParameter",
    full_name="apollo.drivers.lidar.LidarParameter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="brand",
            full_name="apollo.drivers.lidar.LidarParameter.brand",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=2,
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_LIDARPARAMETER_LIDARBRAND, _LIDARPARAMETER_LIDARCHANNELID],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=76,
    serialized_end=311,
)
_LIDARPARAMETER.fields_by_name["brand"].enum_type = _LIDARPARAMETER_LIDARBRAND
_LIDARPARAMETER_LIDARBRAND.containing_type = _LIDARPARAMETER
_LIDARPARAMETER_LIDARCHANNELID.containing_type = _LIDARPARAMETER
DESCRIPTOR.message_types_by_name["LidarParameter"] = _LIDARPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
LidarParameter = _reflection.GeneratedProtocolMessageType(
    "LidarParameter",
    (_message.Message,),
    {
        "DESCRIPTOR": _LIDARPARAMETER,
        "__module__": "modules.drivers.lidar.proto.lidar_parameter_pb2",
    },
)
_sym_db.RegisterMessage(LidarParameter)
