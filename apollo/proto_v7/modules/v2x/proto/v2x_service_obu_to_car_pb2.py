"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.v2x.proto import (
    v2x_monitor_pb2 as modules_dot_v2x_dot_proto_dot_v2x__monitor__pb2,
)
from ....modules.v2x.proto import (
    v2x_obstacles_pb2 as modules_dot_v2x_dot_proto_dot_v2x__obstacles__pb2,
)
from ....modules.v2x.proto import (
    v2x_obu_rsi_pb2 as modules_dot_v2x_dot_proto_dot_v2x__obu__rsi__pb2,
)
from ....modules.v2x.proto import (
    v2x_obu_traffic_light_pb2 as modules_dot_v2x_dot_proto_dot_v2x__obu__traffic__light__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/v2x/proto/v2x_service_obu_to_car.proto",
    package="apollo.v2x",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n.modules/v2x/proto/v2x_service_obu_to_car.proto\x12\napollo.v2x\x1a-modules/v2x/proto/v2x_obu_traffic_light.proto\x1a#modules/v2x/proto/v2x_monitor.proto\x1a#modules/v2x/proto/v2x_obu_rsi.proto\x1a%modules/v2x/proto/v2x_obstacles.proto"I\n\x0eStatusResponse\x12\x15\n\x06status\x18\x01 \x02(\x08:\x05false\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x12\n\nerror_code\x18\x03 \x01(\x032\xbb\x02\n\x08ObuToCar\x12Q\n\x17SendPerceptionObstacles\x12\x18.apollo.v2x.V2XObstacles\x1a\x1a.apollo.v2x.StatusResponse"\x00\x12T\n\x13SendV2xTrafficLight\x12\x1f.apollo.v2x.obu.ObuTrafficLight\x1a\x1a.apollo.v2x.StatusResponse"\x00\x12B\n\nSendV2xRSI\x12\x16.apollo.v2x.obu.ObuRsi\x1a\x1a.apollo.v2x.StatusResponse"\x00\x12B\n\x0cSendObuAlarm\x12\x14.apollo.v2x.ObuAlarm\x1a\x1a.apollo.v2x.StatusResponse"\x00',
    dependencies=[
        modules_dot_v2x_dot_proto_dot_v2x__obu__traffic__light__pb2.DESCRIPTOR,
        modules_dot_v2x_dot_proto_dot_v2x__monitor__pb2.DESCRIPTOR,
        modules_dot_v2x_dot_proto_dot_v2x__obu__rsi__pb2.DESCRIPTOR,
        modules_dot_v2x_dot_proto_dot_v2x__obstacles__pb2.DESCRIPTOR,
    ],
)
_STATUSRESPONSE = _descriptor.Descriptor(
    name="StatusResponse",
    full_name="apollo.v2x.StatusResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="status",
            full_name="apollo.v2x.StatusResponse.status",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=2,
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
            name="info",
            full_name="apollo.v2x.StatusResponse.info",
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
            name="error_code",
            full_name="apollo.v2x.StatusResponse.error_code",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
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
    serialized_start=222,
    serialized_end=295,
)
DESCRIPTOR.message_types_by_name["StatusResponse"] = _STATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
StatusResponse = _reflection.GeneratedProtocolMessageType(
    "StatusResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATUSRESPONSE,
        "__module__": "modules.v2x.proto.v2x_service_obu_to_car_pb2",
    },
)
_sym_db.RegisterMessage(StatusResponse)
_OBUTOCAR = _descriptor.ServiceDescriptor(
    name="ObuToCar",
    full_name="apollo.v2x.ObuToCar",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=298,
    serialized_end=613,
    methods=[
        _descriptor.MethodDescriptor(
            name="SendPerceptionObstacles",
            full_name="apollo.v2x.ObuToCar.SendPerceptionObstacles",
            index=0,
            containing_service=None,
            input_type=modules_dot_v2x_dot_proto_dot_v2x__obstacles__pb2._V2XOBSTACLES,
            output_type=_STATUSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendV2xTrafficLight",
            full_name="apollo.v2x.ObuToCar.SendV2xTrafficLight",
            index=1,
            containing_service=None,
            input_type=modules_dot_v2x_dot_proto_dot_v2x__obu__traffic__light__pb2._OBUTRAFFICLIGHT,
            output_type=_STATUSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendV2xRSI",
            full_name="apollo.v2x.ObuToCar.SendV2xRSI",
            index=2,
            containing_service=None,
            input_type=modules_dot_v2x_dot_proto_dot_v2x__obu__rsi__pb2._OBURSI,
            output_type=_STATUSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SendObuAlarm",
            full_name="apollo.v2x.ObuToCar.SendObuAlarm",
            index=3,
            containing_service=None,
            input_type=modules_dot_v2x_dot_proto_dot_v2x__monitor__pb2._OBUALARM,
            output_type=_STATUSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_OBUTOCAR)
DESCRIPTOR.services_by_name["ObuToCar"] = _OBUTOCAR