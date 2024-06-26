"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/planning_msgs/scenario_type.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n5modules/common_msgs/planning_msgs/scenario_type.proto\x12\x0fapollo.planning*\xa3\x03\n\x0cScenarioType\x12\x0f\n\x0bLANE_FOLLOW\x10\x00\x12!\n\x1dBARE_INTERSECTION_UNPROTECTED\x10\x02\x12\x17\n\x13STOP_SIGN_PROTECTED\x10\x03\x12\x19\n\x15STOP_SIGN_UNPROTECTED\x10\x04\x12\x1b\n\x17TRAFFIC_LIGHT_PROTECTED\x10\x05\x12'\n#TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN\x10\x06\x12(\n$TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN\x10\x07\x12\x0e\n\nYIELD_SIGN\x10\x08\x12\r\n\tPULL_OVER\x10\t\x12\x11\n\rVALET_PARKING\x10\n\x12\x17\n\x13EMERGENCY_PULL_OVER\x10\x0b\x12\x12\n\x0eEMERGENCY_STOP\x10\x0c\x12\x18\n\x14NARROW_STREET_U_TURN\x10\r\x12\x0f\n\x0bPARK_AND_GO\x10\x0e\x12\x19\n\x15LEARNING_MODEL_SAMPLE\x10\x0f\x12\x16\n\x12DEADEND_TURNAROUND\x10\x10*\x9f\n\n\tStageType\x12\x0c\n\x08NO_STAGE\x10\x00\x12\x1d\n\x19LANE_FOLLOW_DEFAULT_STAGE\x10\x01\x12+\n&BARE_INTERSECTION_UNPROTECTED_APPROACH\x10\xc8\x01\x126\n1BARE_INTERSECTION_UNPROTECTED_INTERSECTION_CRUISE\x10\xc9\x01\x12#\n\x1eSTOP_SIGN_UNPROTECTED_PRE_STOP\x10\xac\x02\x12\x1f\n\x1aSTOP_SIGN_UNPROTECTED_STOP\x10\xad\x02\x12 \n\x1bSTOP_SIGN_UNPROTECTED_CREEP\x10\xae\x02\x12.\n)STOP_SIGN_UNPROTECTED_INTERSECTION_CRUISE\x10\xaf\x02\x12%\n TRAFFIC_LIGHT_PROTECTED_APPROACH\x10\x90\x03\x120\n+TRAFFIC_LIGHT_PROTECTED_INTERSECTION_CRUISE\x10\x91\x03\x121\n,TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_APPROACH\x10\x9a\x03\x12.\n)TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_CREEP\x10\x9b\x03\x12<\n7TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_INTERSECTION_CRUISE\x10\x9c\x03\x12.\n)TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_STOP\x10\xa4\x03\x12/\n*TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_CREEP\x10\xa5\x03\x12=\n8TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_INTERSECTION_CRUISE\x10\xa6\x03\x12\x17\n\x12PULL_OVER_APPROACH\x10\xf4\x03\x12%\n PULL_OVER_RETRY_APPROACH_PARKING\x10\xf5\x03\x12\x1c\n\x17PULL_OVER_RETRY_PARKING\x10\xf6\x03\x12\"\n\x1dEMERGENCY_PULL_OVER_SLOW_DOWN\x10\xd8\x04\x12!\n\x1cEMERGENCY_PULL_OVER_APPROACH\x10\xd9\x04\x12 \n\x1bEMERGENCY_PULL_OVER_STANDBY\x10\xda\x04\x12\x1c\n\x17EMERGENCY_STOP_APPROACH\x10\xe2\x04\x12\x1b\n\x16EMERGENCY_STOP_STANDBY\x10\xe3\x04\x12+\n&VALET_PARKING_APPROACHING_PARKING_SPOT\x10\xbc\x05\x12\x1a\n\x15VALET_PARKING_PARKING\x10\xbd\x05\x121\n,DEADEND_TURNAROUND_APPROACHING_TURNING_POINT\x10\xcc\x08\x12\x1f\n\x1aDEADEND_TURNAROUND_TURNING\x10\xcd\x08\x12\x16\n\x11PARK_AND_GO_CHECK\x10\xa0\x06\x12\x17\n\x12PARK_AND_GO_CRUISE\x10\xa1\x06\x12\x17\n\x12PARK_AND_GO_ADJUST\x10\xa2\x06\x12\x1b\n\x16PARK_AND_GO_PRE_CRUISE\x10\xa3\x06\x12\x18\n\x13YIELD_SIGN_APPROACH\x10\x84\x07\x12\x15\n\x10YIELD_SIGN_CREEP\x10\x85\x07\x12\x17\n\x12LEARNING_MODEL_RUN\x10\xe8\x07",
)
_SCENARIOTYPE = _descriptor.EnumDescriptor(
    name="ScenarioType",
    full_name="apollo.planning.ScenarioType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="LANE_FOLLOW",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BARE_INTERSECTION_UNPROTECTED",
            index=1,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP_SIGN_PROTECTED",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP_SIGN_UNPROTECTED",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_PROTECTED",
            index=4,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN",
            index=5,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN",
            index=6,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="YIELD_SIGN",
            index=7,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PULL_OVER",
            index=8,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="VALET_PARKING",
            index=9,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_PULL_OVER",
            index=10,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_STOP",
            index=11,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NARROW_STREET_U_TURN",
            index=12,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK_AND_GO",
            index=13,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LEARNING_MODEL_SAMPLE",
            index=14,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEADEND_TURNAROUND",
            index=15,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=75,
    serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_SCENARIOTYPE)
ScenarioType = enum_type_wrapper.EnumTypeWrapper(_SCENARIOTYPE)
_STAGETYPE = _descriptor.EnumDescriptor(
    name="StageType",
    full_name="apollo.planning.StageType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NO_STAGE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LANE_FOLLOW_DEFAULT_STAGE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BARE_INTERSECTION_UNPROTECTED_APPROACH",
            index=2,
            number=200,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BARE_INTERSECTION_UNPROTECTED_INTERSECTION_CRUISE",
            index=3,
            number=201,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP_SIGN_UNPROTECTED_PRE_STOP",
            index=4,
            number=300,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP_SIGN_UNPROTECTED_STOP",
            index=5,
            number=301,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP_SIGN_UNPROTECTED_CREEP",
            index=6,
            number=302,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STOP_SIGN_UNPROTECTED_INTERSECTION_CRUISE",
            index=7,
            number=303,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_PROTECTED_APPROACH",
            index=8,
            number=400,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_PROTECTED_INTERSECTION_CRUISE",
            index=9,
            number=401,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_APPROACH",
            index=10,
            number=410,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_CREEP",
            index=11,
            number=411,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_INTERSECTION_CRUISE",
            index=12,
            number=412,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_STOP",
            index=13,
            number=420,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_CREEP",
            index=14,
            number=421,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_INTERSECTION_CRUISE",
            index=15,
            number=422,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PULL_OVER_APPROACH",
            index=16,
            number=500,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PULL_OVER_RETRY_APPROACH_PARKING",
            index=17,
            number=501,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PULL_OVER_RETRY_PARKING",
            index=18,
            number=502,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_PULL_OVER_SLOW_DOWN",
            index=19,
            number=600,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_PULL_OVER_APPROACH",
            index=20,
            number=601,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_PULL_OVER_STANDBY",
            index=21,
            number=602,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_STOP_APPROACH",
            index=22,
            number=610,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY_STOP_STANDBY",
            index=23,
            number=611,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="VALET_PARKING_APPROACHING_PARKING_SPOT",
            index=24,
            number=700,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="VALET_PARKING_PARKING",
            index=25,
            number=701,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEADEND_TURNAROUND_APPROACHING_TURNING_POINT",
            index=26,
            number=1100,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEADEND_TURNAROUND_TURNING",
            index=27,
            number=1101,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK_AND_GO_CHECK",
            index=28,
            number=800,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK_AND_GO_CRUISE",
            index=29,
            number=801,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK_AND_GO_ADJUST",
            index=30,
            number=802,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK_AND_GO_PRE_CRUISE",
            index=31,
            number=803,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="YIELD_SIGN_APPROACH",
            index=32,
            number=900,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="YIELD_SIGN_CREEP",
            index=33,
            number=901,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LEARNING_MODEL_RUN",
            index=34,
            number=1000,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=497,
    serialized_end=1808,
)
_sym_db.RegisterEnumDescriptor(_STAGETYPE)
StageType = enum_type_wrapper.EnumTypeWrapper(_STAGETYPE)
LANE_FOLLOW = 0
BARE_INTERSECTION_UNPROTECTED = 2
STOP_SIGN_PROTECTED = 3
STOP_SIGN_UNPROTECTED = 4
TRAFFIC_LIGHT_PROTECTED = 5
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN = 6
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN = 7
YIELD_SIGN = 8
PULL_OVER = 9
VALET_PARKING = 10
EMERGENCY_PULL_OVER = 11
EMERGENCY_STOP = 12
NARROW_STREET_U_TURN = 13
PARK_AND_GO = 14
LEARNING_MODEL_SAMPLE = 15
DEADEND_TURNAROUND = 16
NO_STAGE = 0
LANE_FOLLOW_DEFAULT_STAGE = 1
BARE_INTERSECTION_UNPROTECTED_APPROACH = 200
BARE_INTERSECTION_UNPROTECTED_INTERSECTION_CRUISE = 201
STOP_SIGN_UNPROTECTED_PRE_STOP = 300
STOP_SIGN_UNPROTECTED_STOP = 301
STOP_SIGN_UNPROTECTED_CREEP = 302
STOP_SIGN_UNPROTECTED_INTERSECTION_CRUISE = 303
TRAFFIC_LIGHT_PROTECTED_APPROACH = 400
TRAFFIC_LIGHT_PROTECTED_INTERSECTION_CRUISE = 401
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_APPROACH = 410
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_CREEP = 411
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_INTERSECTION_CRUISE = 412
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_STOP = 420
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_CREEP = 421
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_INTERSECTION_CRUISE = 422
PULL_OVER_APPROACH = 500
PULL_OVER_RETRY_APPROACH_PARKING = 501
PULL_OVER_RETRY_PARKING = 502
EMERGENCY_PULL_OVER_SLOW_DOWN = 600
EMERGENCY_PULL_OVER_APPROACH = 601
EMERGENCY_PULL_OVER_STANDBY = 602
EMERGENCY_STOP_APPROACH = 610
EMERGENCY_STOP_STANDBY = 611
VALET_PARKING_APPROACHING_PARKING_SPOT = 700
VALET_PARKING_PARKING = 701
DEADEND_TURNAROUND_APPROACHING_TURNING_POINT = 1100
DEADEND_TURNAROUND_TURNING = 1101
PARK_AND_GO_CHECK = 800
PARK_AND_GO_CRUISE = 801
PARK_AND_GO_ADJUST = 802
PARK_AND_GO_PRE_CRUISE = 803
YIELD_SIGN_APPROACH = 900
YIELD_SIGN_CREEP = 901
LEARNING_MODEL_RUN = 1000
DESCRIPTOR.enum_types_by_name["ScenarioType"] = _SCENARIOTYPE
DESCRIPTOR.enum_types_by_name["StageType"] = _STAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
