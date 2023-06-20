"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2,
)
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)
from ....modules.common_msgs.perception_msgs import (
    perception_obstacle_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2,
)
from ....modules.common_msgs.prediction_msgs import (
    feature_pb2 as modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2,
)
from ....modules.common_msgs.prediction_msgs import (
    scenario_pb2 as modules_dot_common__msgs_dot_prediction__msgs_dot_scenario__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/prediction_msgs/prediction_obstacle.proto",
    package="apollo.prediction",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n=modules/common_msgs/prediction_msgs/prediction_obstacle.proto\x12\x11apollo.prediction\x1a/modules/common_msgs/basic_msgs/error_code.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a=modules/common_msgs/perception_msgs/perception_obstacle.proto\x1a2modules/common_msgs/prediction_msgs/scenario.proto\x1a1modules/common_msgs/prediction_msgs/feature.proto"\xf6\x01\n\x0eObstacleIntent\x12=\n\x04type\x18\x01 \x01(\x0e2&.apollo.prediction.ObstacleIntent.Type:\x07UNKNOWN"\xa4\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\x0e\n\nSTATIONARY\x10\x02\x12\n\n\x06MOVING\x10\x03\x12\x0f\n\x0bCHANGE_LANE\x10\x04\x12\x14\n\x10LOW_ACCELERATION\x10\x05\x12\x15\n\x11HIGH_ACCELERATION\x10\x06\x12\x14\n\x10LOW_DECELERATION\x10\x07\x12\x15\n\x11HIGH_DECELERATION\x10\x08"{\n\x06Intent\x125\n\x04type\x18\x01 \x01(\x0e2\x1e.apollo.prediction.Intent.Type:\x07UNKNOWN":\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04STOP\x10\x01\x12\n\n\x06CRUISE\x10\x02\x12\x0f\n\x0bCHANGE_LANE\x10\x03"\xad\x03\n\x12PredictionObstacle\x12B\n\x13perception_obstacle\x18\x01 \x01(\x0b2%.apollo.perception.PerceptionObstacle\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x18\n\x10predicted_period\x18\x03 \x01(\x01\x121\n\ntrajectory\x18\x04 \x03(\x0b2\x1d.apollo.prediction.Trajectory\x121\n\x06intent\x18\x05 \x01(\x0b2!.apollo.prediction.ObstacleIntent\x125\n\x08priority\x18\x06 \x01(\x0b2#.apollo.prediction.ObstaclePriority\x12B\n\x0finteractive_tag\x18\t \x01(\x0b2).apollo.prediction.ObstacleInteractiveTag\x12\x18\n\tis_static\x18\x07 \x01(\x08:\x05false\x12+\n\x07feature\x18\x08 \x03(\x0b2\x1a.apollo.prediction.Feature"\xc3\x02\n\x13PredictionObstacles\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12B\n\x13prediction_obstacle\x18\x02 \x03(\x0b2%.apollo.prediction.PredictionObstacle\x127\n\x15perception_error_code\x18\x03 \x01(\x0e2\x18.apollo.common.ErrorCode\x12\x17\n\x0fstart_timestamp\x18\x04 \x01(\x01\x12\x15\n\rend_timestamp\x18\x05 \x01(\x01\x12)\n\x06intent\x18\x06 \x01(\x0b2\x19.apollo.prediction.Intent\x12-\n\x08scenario\x18\x07 \x01(\x0b2\x1b.apollo.prediction.Scenario',
    dependencies=[
        modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_prediction__msgs_dot_scenario__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2.DESCRIPTOR,
    ],
)
_OBSTACLEINTENT_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.prediction.ObstacleIntent.Type",
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
            name="STOP",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STATIONARY",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MOVING",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANGE_LANE",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOW_ACCELERATION",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HIGH_ACCELERATION",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOW_DECELERATION",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HIGH_DECELERATION",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=427,
    serialized_end=591,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLEINTENT_TYPE)
_INTENT_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="apollo.prediction.Intent.Type",
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
            name="STOP",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CRUISE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CHANGE_LANE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=658,
    serialized_end=716,
)
_sym_db.RegisterEnumDescriptor(_INTENT_TYPE)
_OBSTACLEINTENT = _descriptor.Descriptor(
    name="ObstacleIntent",
    full_name="apollo.prediction.ObstacleIntent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="apollo.prediction.ObstacleIntent.type",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_OBSTACLEINTENT_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=345,
    serialized_end=591,
)
_INTENT = _descriptor.Descriptor(
    name="Intent",
    full_name="apollo.prediction.Intent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="apollo.prediction.Intent.type",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_INTENT_TYPE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=593,
    serialized_end=716,
)
_PREDICTIONOBSTACLE = _descriptor.Descriptor(
    name="PredictionObstacle",
    full_name="apollo.prediction.PredictionObstacle",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="perception_obstacle",
            full_name="apollo.prediction.PredictionObstacle.perception_obstacle",
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
            name="timestamp",
            full_name="apollo.prediction.PredictionObstacle.timestamp",
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
            name="predicted_period",
            full_name="apollo.prediction.PredictionObstacle.predicted_period",
            index=2,
            number=3,
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
            name="trajectory",
            full_name="apollo.prediction.PredictionObstacle.trajectory",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="intent",
            full_name="apollo.prediction.PredictionObstacle.intent",
            index=4,
            number=5,
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
            name="priority",
            full_name="apollo.prediction.PredictionObstacle.priority",
            index=5,
            number=6,
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
            name="interactive_tag",
            full_name="apollo.prediction.PredictionObstacle.interactive_tag",
            index=6,
            number=9,
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
            name="is_static",
            full_name="apollo.prediction.PredictionObstacle.is_static",
            index=7,
            number=7,
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
            name="feature",
            full_name="apollo.prediction.PredictionObstacle.feature",
            index=8,
            number=8,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=719,
    serialized_end=1148,
)
_PREDICTIONOBSTACLES = _descriptor.Descriptor(
    name="PredictionObstacles",
    full_name="apollo.prediction.PredictionObstacles",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.prediction.PredictionObstacles.header",
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
            name="prediction_obstacle",
            full_name="apollo.prediction.PredictionObstacles.prediction_obstacle",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="perception_error_code",
            full_name="apollo.prediction.PredictionObstacles.perception_error_code",
            index=2,
            number=3,
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
            name="start_timestamp",
            full_name="apollo.prediction.PredictionObstacles.start_timestamp",
            index=3,
            number=4,
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
            name="end_timestamp",
            full_name="apollo.prediction.PredictionObstacles.end_timestamp",
            index=4,
            number=5,
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
            name="intent",
            full_name="apollo.prediction.PredictionObstacles.intent",
            index=5,
            number=6,
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
            name="scenario",
            full_name="apollo.prediction.PredictionObstacles.scenario",
            index=6,
            number=7,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1151,
    serialized_end=1474,
)
_OBSTACLEINTENT.fields_by_name["type"].enum_type = _OBSTACLEINTENT_TYPE
_OBSTACLEINTENT_TYPE.containing_type = _OBSTACLEINTENT
_INTENT.fields_by_name["type"].enum_type = _INTENT_TYPE
_INTENT_TYPE.containing_type = _INTENT
_PREDICTIONOBSTACLE.fields_by_name[
    "perception_obstacle"
].message_type = (
    modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2._PERCEPTIONOBSTACLE
)
_PREDICTIONOBSTACLE.fields_by_name[
    "trajectory"
].message_type = (
    modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2._TRAJECTORY
)
_PREDICTIONOBSTACLE.fields_by_name["intent"].message_type = _OBSTACLEINTENT
_PREDICTIONOBSTACLE.fields_by_name[
    "priority"
].message_type = (
    modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2._OBSTACLEPRIORITY
)
_PREDICTIONOBSTACLE.fields_by_name[
    "interactive_tag"
].message_type = (
    modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2._OBSTACLEINTERACTIVETAG
)
_PREDICTIONOBSTACLE.fields_by_name[
    "feature"
].message_type = modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2._FEATURE
_PREDICTIONOBSTACLES.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_PREDICTIONOBSTACLES.fields_by_name[
    "prediction_obstacle"
].message_type = _PREDICTIONOBSTACLE
_PREDICTIONOBSTACLES.fields_by_name[
    "perception_error_code"
].enum_type = modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2._ERRORCODE
_PREDICTIONOBSTACLES.fields_by_name["intent"].message_type = _INTENT
_PREDICTIONOBSTACLES.fields_by_name[
    "scenario"
].message_type = (
    modules_dot_common__msgs_dot_prediction__msgs_dot_scenario__pb2._SCENARIO
)
DESCRIPTOR.message_types_by_name["ObstacleIntent"] = _OBSTACLEINTENT
DESCRIPTOR.message_types_by_name["Intent"] = _INTENT
DESCRIPTOR.message_types_by_name["PredictionObstacle"] = _PREDICTIONOBSTACLE
DESCRIPTOR.message_types_by_name["PredictionObstacles"] = _PREDICTIONOBSTACLES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ObstacleIntent = _reflection.GeneratedProtocolMessageType(
    "ObstacleIntent",
    (_message.Message,),
    {
        "DESCRIPTOR": _OBSTACLEINTENT,
        "__module__": "modules.common_msgs.prediction_msgs.prediction_obstacle_pb2",
    },
)
_sym_db.RegisterMessage(ObstacleIntent)
Intent = _reflection.GeneratedProtocolMessageType(
    "Intent",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTENT,
        "__module__": "modules.common_msgs.prediction_msgs.prediction_obstacle_pb2",
    },
)
_sym_db.RegisterMessage(Intent)
PredictionObstacle = _reflection.GeneratedProtocolMessageType(
    "PredictionObstacle",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREDICTIONOBSTACLE,
        "__module__": "modules.common_msgs.prediction_msgs.prediction_obstacle_pb2",
    },
)
_sym_db.RegisterMessage(PredictionObstacle)
PredictionObstacles = _reflection.GeneratedProtocolMessageType(
    "PredictionObstacles",
    (_message.Message,),
    {
        "DESCRIPTOR": _PREDICTIONOBSTACLES,
        "__module__": "modules.common_msgs.prediction_msgs.prediction_obstacle_pb2",
    },
)
_sym_db.RegisterMessage(PredictionObstacles)
