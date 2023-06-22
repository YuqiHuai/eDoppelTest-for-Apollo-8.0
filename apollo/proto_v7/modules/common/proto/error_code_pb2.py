"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common/proto/error_code.proto",
    package="apollo.common",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n%modules/common/proto/error_code.proto\x12\rapollo.common\"I\n\x08StatusPb\x120\n\nerror_code\x18\x01 \x01(\x0e2\x18.apollo.common.ErrorCode:\x02OK\x12\x0b\n\x03msg\x18\x02 \x01(\t*\x99\x08\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x12\n\rCONTROL_ERROR\x10\xe8\x07\x12\x17\n\x12CONTROL_INIT_ERROR\x10\xe9\x07\x12\x1a\n\x15CONTROL_COMPUTE_ERROR\x10\xea\x07\x12\x18\n\x13CONTROL_ESTOP_ERROR\x10\xeb\x07\x12\x1a\n\x15PERFECT_CONTROL_ERROR\x10\xec\x07\x12\x11\n\x0cCANBUS_ERROR\x10\xd0\x0f\x12\x1a\n\x15CAN_CLIENT_ERROR_BASE\x10\xb4\x10\x12(\n#CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED\x10\xb5\x10\x12\x1f\n\x1aCAN_CLIENT_ERROR_FRAME_NUM\x10\xb6\x10\x12!\n\x1cCAN_CLIENT_ERROR_SEND_FAILED\x10\xb7\x10\x12!\n\x1cCAN_CLIENT_ERROR_RECV_FAILED\x10\xb8\x10\x12\x17\n\x12LOCALIZATION_ERROR\x10\xb8\x17\x12\x1b\n\x16LOCALIZATION_ERROR_MSG\x10\x9c\x18\x12\x1d\n\x18LOCALIZATION_ERROR_LIDAR\x10\x80\x19\x12\x1d\n\x18LOCALIZATION_ERROR_INTEG\x10\xe4\x19\x12\x1c\n\x17LOCALIZATION_ERROR_GNSS\x10\xc8\x1a\x12\x15\n\x10PERCEPTION_ERROR\x10\xa0\x1f\x12\x18\n\x13PERCEPTION_ERROR_TF\x10\xa1\x1f\x12\x1d\n\x18PERCEPTION_ERROR_PROCESS\x10\xa2\x1f\x12\x15\n\x10PERCEPTION_FATAL\x10\xa3\x1f\x12\x1a\n\x15PERCEPTION_ERROR_NONE\x10\xa4\x1f\x12\x1d\n\x18PERCEPTION_ERROR_UNKNOWN\x10\xa5\x1f\x12\x15\n\x10PREDICTION_ERROR\x10\x88'\x12\x13\n\x0ePLANNING_ERROR\x10\xf0.\x12\x1d\n\x18PLANNING_ERROR_NOT_READY\x10\xf1.\x12\x15\n\x10HDMAP_DATA_ERROR\x10\xd86\x12\x12\n\rROUTING_ERROR\x10\xc0>\x12\x1a\n\x15ROUTING_ERROR_REQUEST\x10\xc1>\x12\x1b\n\x16ROUTING_ERROR_RESPONSE\x10\xc2>\x12\x1c\n\x17ROUTING_ERROR_NOT_READY\x10\xc3>\x12\x11\n\x0cEND_OF_INPUT\x10\xa8F\x12\x15\n\x10HTTP_LOGIC_ERROR\x10\x90N\x12\x17\n\x12HTTP_RUNTIME_ERROR\x10\x91N\x12\x17\n\x12RELATIVE_MAP_ERROR\x10\xf8U\x12\x1b\n\x16RELATIVE_MAP_NOT_READY\x10\xf9U\x12\x16\n\x11DRIVER_ERROR_GNSS\x10\xe0]\x12\x1a\n\x15DRIVER_ERROR_VELODYNE\x10\xc8e\x12\x17\n\x12STORYTELLING_ERROR\x10\xb0m",
)
_ERRORCODE = _descriptor.EnumDescriptor(
    name="ErrorCode",
    full_name="apollo.common.ErrorCode",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="OK",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTROL_ERROR",
            index=1,
            number=1000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTROL_INIT_ERROR",
            index=2,
            number=1001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTROL_COMPUTE_ERROR",
            index=3,
            number=1002,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTROL_ESTOP_ERROR",
            index=4,
            number=1003,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERFECT_CONTROL_ERROR",
            index=5,
            number=1004,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CANBUS_ERROR",
            index=6,
            number=2000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CAN_CLIENT_ERROR_BASE",
            index=7,
            number=2100,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED",
            index=8,
            number=2101,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CAN_CLIENT_ERROR_FRAME_NUM",
            index=9,
            number=2102,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CAN_CLIENT_ERROR_SEND_FAILED",
            index=10,
            number=2103,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CAN_CLIENT_ERROR_RECV_FAILED",
            index=11,
            number=2104,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCALIZATION_ERROR",
            index=12,
            number=3000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCALIZATION_ERROR_MSG",
            index=13,
            number=3100,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCALIZATION_ERROR_LIDAR",
            index=14,
            number=3200,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCALIZATION_ERROR_INTEG",
            index=15,
            number=3300,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCALIZATION_ERROR_GNSS",
            index=16,
            number=3400,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERCEPTION_ERROR",
            index=17,
            number=4000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERCEPTION_ERROR_TF",
            index=18,
            number=4001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERCEPTION_ERROR_PROCESS",
            index=19,
            number=4002,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERCEPTION_FATAL",
            index=20,
            number=4003,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERCEPTION_ERROR_NONE",
            index=21,
            number=4004,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERCEPTION_ERROR_UNKNOWN",
            index=22,
            number=4005,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PREDICTION_ERROR",
            index=23,
            number=5000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PLANNING_ERROR",
            index=24,
            number=6000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PLANNING_ERROR_NOT_READY",
            index=25,
            number=6001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HDMAP_DATA_ERROR",
            index=26,
            number=7000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROUTING_ERROR",
            index=27,
            number=8000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROUTING_ERROR_REQUEST",
            index=28,
            number=8001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROUTING_ERROR_RESPONSE",
            index=29,
            number=8002,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROUTING_ERROR_NOT_READY",
            index=30,
            number=8003,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="END_OF_INPUT",
            index=31,
            number=9000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HTTP_LOGIC_ERROR",
            index=32,
            number=10000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HTTP_RUNTIME_ERROR",
            index=33,
            number=10001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RELATIVE_MAP_ERROR",
            index=34,
            number=11000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RELATIVE_MAP_NOT_READY",
            index=35,
            number=11001,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DRIVER_ERROR_GNSS",
            index=36,
            number=12000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DRIVER_ERROR_VELODYNE",
            index=37,
            number=13000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STORYTELLING_ERROR",
            index=38,
            number=14000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=132,
    serialized_end=1181,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
OK = 0
CONTROL_ERROR = 1000
CONTROL_INIT_ERROR = 1001
CONTROL_COMPUTE_ERROR = 1002
CONTROL_ESTOP_ERROR = 1003
PERFECT_CONTROL_ERROR = 1004
CANBUS_ERROR = 2000
CAN_CLIENT_ERROR_BASE = 2100
CAN_CLIENT_ERROR_OPEN_DEVICE_FAILED = 2101
CAN_CLIENT_ERROR_FRAME_NUM = 2102
CAN_CLIENT_ERROR_SEND_FAILED = 2103
CAN_CLIENT_ERROR_RECV_FAILED = 2104
LOCALIZATION_ERROR = 3000
LOCALIZATION_ERROR_MSG = 3100
LOCALIZATION_ERROR_LIDAR = 3200
LOCALIZATION_ERROR_INTEG = 3300
LOCALIZATION_ERROR_GNSS = 3400
PERCEPTION_ERROR = 4000
PERCEPTION_ERROR_TF = 4001
PERCEPTION_ERROR_PROCESS = 4002
PERCEPTION_FATAL = 4003
PERCEPTION_ERROR_NONE = 4004
PERCEPTION_ERROR_UNKNOWN = 4005
PREDICTION_ERROR = 5000
PLANNING_ERROR = 6000
PLANNING_ERROR_NOT_READY = 6001
HDMAP_DATA_ERROR = 7000
ROUTING_ERROR = 8000
ROUTING_ERROR_REQUEST = 8001
ROUTING_ERROR_RESPONSE = 8002
ROUTING_ERROR_NOT_READY = 8003
END_OF_INPUT = 9000
HTTP_LOGIC_ERROR = 10000
HTTP_RUNTIME_ERROR = 10001
RELATIVE_MAP_ERROR = 11000
RELATIVE_MAP_NOT_READY = 11001
DRIVER_ERROR_GNSS = 12000
DRIVER_ERROR_VELODYNE = 13000
STORYTELLING_ERROR = 14000
_STATUSPB = _descriptor.Descriptor(
    name="StatusPb",
    full_name="apollo.common.StatusPb",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="error_code",
            full_name="apollo.common.StatusPb.error_code",
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
            name="msg",
            full_name="apollo.common.StatusPb.msg",
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
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=56,
    serialized_end=129,
)
_STATUSPB.fields_by_name["error_code"].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name["StatusPb"] = _STATUSPB
DESCRIPTOR.enum_types_by_name["ErrorCode"] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
StatusPb = _reflection.GeneratedProtocolMessageType(
    "StatusPb",
    (_message.Message,),
    {"DESCRIPTOR": _STATUSPB, "__module__": "modules.common.proto.error_code_pb2"},
)
_sym_db.RegisterMessage(StatusPb)