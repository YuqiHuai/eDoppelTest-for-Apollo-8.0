"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/localization_msgs/localization_status.proto",
    package="apollo.localization",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n?modules/common_msgs/localization_msgs/localization_status.proto\x12\x13apollo.localization"\xdc\x01\n\x12MsfSensorMsgStatus\x12@\n\x10imu_delay_status\x18\x01 \x01(\x0e2&.apollo.localization.ImuMsgDelayStatus\x12D\n\x12imu_missing_status\x18\x02 \x01(\x0e2(.apollo.localization.ImuMsgMissingStatus\x12>\n\x0fimu_data_status\x18\x03 \x01(\x0e2%.apollo.localization.ImuMsgDataStatus"\xa9\x03\n\tMsfStatus\x12K\n\x17local_lidar_consistency\x18\x01 \x01(\x0e2*.apollo.localization.LocalLidarConsistency\x12>\n\x10gnss_consistency\x18\x02 \x01(\x0e2$.apollo.localization.GnssConsistency\x12A\n\x12local_lidar_status\x18\x03 \x01(\x0e2%.apollo.localization.LocalLidarStatus\x12C\n\x13local_lidar_quality\x18\x04 \x01(\x0e2&.apollo.localization.LocalLidarQuality\x12D\n\x15gnsspos_position_type\x18\x05 \x01(\x0e2%.apollo.localization.GnssPositionType\x12A\n\x12msf_running_status\x18\x06 \x01(\x0e2%.apollo.localization.MsfRunningStatus*\xa2\x02\n\x10LocalLidarStatus\x12\x1a\n\x16MSF_LOCAL_LIDAR_NORMAL\x10\x00\x12\x1f\n\x1bMSF_LOCAL_LIDAR_MAP_MISSING\x10\x01\x12&\n"MSF_LOCAL_LIDAR_EXTRINSICS_MISSING\x10\x02\x12&\n"MSF_LOCAL_LIDAR_MAP_LOADING_FAILED\x10\x03\x12\x1d\n\x19MSF_LOCAL_LIDAR_NO_OUTPUT\x10\x04\x12\x1e\n\x1aMSF_LOCAL_LIDAR_OUT_OF_MAP\x10\x05\x12\x1c\n\x18MSF_LOCAL_LIDAR_NOT_GOOD\x10\x06\x12$\n MSF_LOCAL_LIDAR_UNDEFINED_STATUS\x10\x07*\x82\x01\n\x11LocalLidarQuality\x12\x1d\n\x19MSF_LOCAL_LIDAR_VERY_GOOD\x10\x00\x12\x18\n\x14MSF_LOCAL_LIDAR_GOOD\x10\x01\x12\x1b\n\x17MSF_LOCAL_LIDAR_NOT_BAD\x10\x02\x12\x17\n\x13MSF_LOCAL_LIDAR_BAD\x10\x03*\xa7\x01\n\x15LocalLidarConsistency\x12"\n\x1eMSF_LOCAL_LIDAR_CONSISTENCY_00\x10\x00\x12"\n\x1eMSF_LOCAL_LIDAR_CONSISTENCY_01\x10\x01\x12"\n\x1eMSF_LOCAL_LIDAR_CONSISTENCY_02\x10\x02\x12"\n\x1eMSF_LOCAL_LIDAR_CONSISTENCY_03\x10\x03*\x85\x01\n\x0fGnssConsistency\x12\x1b\n\x17MSF_GNSS_CONSISTENCY_00\x10\x00\x12\x1b\n\x17MSF_GNSS_CONSISTENCY_01\x10\x01\x12\x1b\n\x17MSF_GNSS_CONSISTENCY_02\x10\x02\x12\x1b\n\x17MSF_GNSS_CONSISTENCY_03\x10\x03*\xb1\x04\n\x10GnssPositionType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08FIXEDPOS\x10\x01\x12\x0f\n\x0bFIXEDHEIGHT\x10\x02\x12\r\n\tFLOATCONV\x10\x04\x12\x0c\n\x08WIDELANE\x10\x05\x12\x0e\n\nNARROWLANE\x10\x06\x12\x14\n\x10DOPPLER_VELOCITY\x10\x08\x12\n\n\x06SINGLE\x10\x10\x12\x0b\n\x07PSRDIFF\x10\x11\x12\x08\n\x04WAAS\x10\x12\x12\x0e\n\nPROPOGATED\x10\x13\x12\x0c\n\x08OMNISTAR\x10\x14\x12\x0c\n\x08L1_FLOAT\x10 \x12\x12\n\x0eIONOFREE_FLOAT\x10!\x12\x10\n\x0cNARROW_FLOAT\x10"\x12\n\n\x06L1_INT\x100\x12\x0c\n\x08WIDE_INT\x101\x12\x0e\n\nNARROW_INT\x102\x12\x12\n\x0eRTK_DIRECT_INS\x103\x12\x0c\n\x08INS_SBAS\x104\x12\r\n\tINS_PSRSP\x105\x12\x0f\n\x0bINS_PSRDIFF\x106\x12\x10\n\x0cINS_RTKFLOAT\x107\x12\x10\n\x0cINS_RTKFIXED\x108\x12\x10\n\x0cINS_OMNISTAR\x109\x12\x13\n\x0fINS_OMNISTAR_HP\x10:\x12\x13\n\x0fINS_OMNISTAR_XP\x10;\x12\x0f\n\x0bOMNISTAR_HP\x10@\x12\x0f\n\x0bOMNISTAR_XP\x10A\x12\x12\n\x0ePPP_CONVERGING\x10D\x12\x07\n\x03PPP\x10E\x12\x16\n\x12INS_PPP_Converging\x10I\x12\x0b\n\x07INS_PPP\x10J\x12\x0c\n\x08MSG_LOSS\x10[*t\n\x11ImuMsgDelayStatus\x12\x14\n\x10IMU_DELAY_NORMAL\x10\x00\x12\x0f\n\x0bIMU_DELAY_1\x10\x01\x12\x0f\n\x0bIMU_DELAY_2\x10\x02\x12\x0f\n\x0bIMU_DELAY_3\x10\x03\x12\x16\n\x12IMU_DELAY_ABNORMAL\x10\x04*\xa6\x01\n\x13ImuMsgMissingStatus\x12\x16\n\x12IMU_MISSING_NORMAL\x10\x00\x12\x11\n\rIMU_MISSING_1\x10\x01\x12\x11\n\rIMU_MISSING_2\x10\x02\x12\x11\n\rIMU_MISSING_3\x10\x03\x12\x11\n\rIMU_MISSING_4\x10\x04\x12\x11\n\rIMU_MISSING_5\x10\x05\x12\x18\n\x14IMU_MISSING_ABNORMAL\x10\x06*R\n\x10ImuMsgDataStatus\x12\x13\n\x0fIMU_DATA_NORMAL\x10\x00\x12\x15\n\x11IMU_DATA_ABNORMAL\x10\x01\x12\x12\n\x0eIMU_DATA_OTHER\x10\x02*\xac\x04\n\x10MsfRunningStatus\x12\x16\n\x12MSF_SOL_LIDAR_GNSS\x10\x00\x12\x12\n\x0eMSF_SOL_X_GNSS\x10\x01\x12\x13\n\x0fMSF_SOL_LIDAR_X\x10\x02\x12\x14\n\x10MSF_SOL_LIDAR_XX\x10\x03\x12\x15\n\x11MSF_SOL_LIDAR_XXX\x10\x04\x12\x0f\n\x0bMSF_SOL_X_X\x10\x05\x12\x10\n\x0cMSF_SOL_X_XX\x10\x06\x12\x11\n\rMSF_SOL_X_XXX\x10\x07\x12\x17\n\x13MSF_SSOL_LIDAR_GNSS\x10\x08\x12\x13\n\x0fMSF_SSOL_X_GNSS\x10\t\x12\x14\n\x10MSF_SSOL_LIDAR_X\x10\n\x12\x15\n\x11MSF_SSOL_LIDAR_XX\x10\x0b\x12\x16\n\x12MSF_SSOL_LIDAR_XXX\x10\x0c\x12\x10\n\x0cMSF_SSOL_X_X\x10\r\x12\x11\n\rMSF_SSOL_X_XX\x10\x0e\x12\x12\n\x0eMSF_SSOL_X_XXX\x10\x0f\x12\x18\n\x14MSF_NOSOL_LIDAR_GNSS\x10\x10\x12\x14\n\x10MSF_NOSOL_X_GNSS\x10\x11\x12\x15\n\x11MSF_NOSOL_LIDAR_X\x10\x12\x12\x16\n\x12MSF_NOSOL_LIDAR_XX\x10\x13\x12\x17\n\x13MSF_NOSOL_LIDAR_XXX\x10\x14\x12\x11\n\rMSF_NOSOL_X_X\x10\x15\x12\x12\n\x0eMSF_NOSOL_X_XX\x10\x16\x12\x13\n\x0fMSF_NOSOL_X_XXX\x10\x17\x12\x14\n\x10MSF_RUNNING_INIT\x10\x18',
)
_LOCALLIDARSTATUS = _descriptor.EnumDescriptor(
    name="LocalLidarStatus",
    full_name="apollo.localization.LocalLidarStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_NORMAL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_MAP_MISSING",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_EXTRINSICS_MISSING",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_MAP_LOADING_FAILED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_NO_OUTPUT",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_OUT_OF_MAP",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_NOT_GOOD",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_UNDEFINED_STATUS",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=740,
    serialized_end=1030,
)
_sym_db.RegisterEnumDescriptor(_LOCALLIDARSTATUS)
LocalLidarStatus = enum_type_wrapper.EnumTypeWrapper(_LOCALLIDARSTATUS)
_LOCALLIDARQUALITY = _descriptor.EnumDescriptor(
    name="LocalLidarQuality",
    full_name="apollo.localization.LocalLidarQuality",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_VERY_GOOD",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_GOOD",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_NOT_BAD",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_BAD",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1033,
    serialized_end=1163,
)
_sym_db.RegisterEnumDescriptor(_LOCALLIDARQUALITY)
LocalLidarQuality = enum_type_wrapper.EnumTypeWrapper(_LOCALLIDARQUALITY)
_LOCALLIDARCONSISTENCY = _descriptor.EnumDescriptor(
    name="LocalLidarConsistency",
    full_name="apollo.localization.LocalLidarConsistency",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_CONSISTENCY_00",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_CONSISTENCY_01",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_CONSISTENCY_02",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_LOCAL_LIDAR_CONSISTENCY_03",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1166,
    serialized_end=1333,
)
_sym_db.RegisterEnumDescriptor(_LOCALLIDARCONSISTENCY)
LocalLidarConsistency = enum_type_wrapper.EnumTypeWrapper(_LOCALLIDARCONSISTENCY)
_GNSSCONSISTENCY = _descriptor.EnumDescriptor(
    name="GnssConsistency",
    full_name="apollo.localization.GnssConsistency",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MSF_GNSS_CONSISTENCY_00",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_GNSS_CONSISTENCY_01",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_GNSS_CONSISTENCY_02",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_GNSS_CONSISTENCY_03",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1336,
    serialized_end=1469,
)
_sym_db.RegisterEnumDescriptor(_GNSSCONSISTENCY)
GnssConsistency = enum_type_wrapper.EnumTypeWrapper(_GNSSCONSISTENCY)
_GNSSPOSITIONTYPE = _descriptor.EnumDescriptor(
    name="GnssPositionType",
    full_name="apollo.localization.GnssPositionType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NONE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FIXEDPOS",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FIXEDHEIGHT",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FLOATCONV",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WIDELANE",
            index=4,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NARROWLANE",
            index=5,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DOPPLER_VELOCITY",
            index=6,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SINGLE",
            index=7,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PSRDIFF",
            index=8,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WAAS",
            index=9,
            number=18,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PROPOGATED",
            index=10,
            number=19,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OMNISTAR",
            index=11,
            number=20,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="L1_FLOAT",
            index=12,
            number=32,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IONOFREE_FLOAT",
            index=13,
            number=33,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NARROW_FLOAT",
            index=14,
            number=34,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="L1_INT",
            index=15,
            number=48,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WIDE_INT",
            index=16,
            number=49,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NARROW_INT",
            index=17,
            number=50,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RTK_DIRECT_INS",
            index=18,
            number=51,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_SBAS",
            index=19,
            number=52,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_PSRSP",
            index=20,
            number=53,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_PSRDIFF",
            index=21,
            number=54,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_RTKFLOAT",
            index=22,
            number=55,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_RTKFIXED",
            index=23,
            number=56,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_OMNISTAR",
            index=24,
            number=57,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_OMNISTAR_HP",
            index=25,
            number=58,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_OMNISTAR_XP",
            index=26,
            number=59,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OMNISTAR_HP",
            index=27,
            number=64,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OMNISTAR_XP",
            index=28,
            number=65,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PPP_CONVERGING",
            index=29,
            number=68,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PPP",
            index=30,
            number=69,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_PPP_Converging",
            index=31,
            number=73,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INS_PPP",
            index=32,
            number=74,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSG_LOSS",
            index=33,
            number=91,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1472,
    serialized_end=2033,
)
_sym_db.RegisterEnumDescriptor(_GNSSPOSITIONTYPE)
GnssPositionType = enum_type_wrapper.EnumTypeWrapper(_GNSSPOSITIONTYPE)
_IMUMSGDELAYSTATUS = _descriptor.EnumDescriptor(
    name="ImuMsgDelayStatus",
    full_name="apollo.localization.ImuMsgDelayStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="IMU_DELAY_NORMAL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_DELAY_1",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_DELAY_2",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_DELAY_3",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_DELAY_ABNORMAL",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=2035,
    serialized_end=2151,
)
_sym_db.RegisterEnumDescriptor(_IMUMSGDELAYSTATUS)
ImuMsgDelayStatus = enum_type_wrapper.EnumTypeWrapper(_IMUMSGDELAYSTATUS)
_IMUMSGMISSINGSTATUS = _descriptor.EnumDescriptor(
    name="ImuMsgMissingStatus",
    full_name="apollo.localization.ImuMsgMissingStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_NORMAL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_1",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_2",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_3",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_4",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_5",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_MISSING_ABNORMAL",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=2154,
    serialized_end=2320,
)
_sym_db.RegisterEnumDescriptor(_IMUMSGMISSINGSTATUS)
ImuMsgMissingStatus = enum_type_wrapper.EnumTypeWrapper(_IMUMSGMISSINGSTATUS)
_IMUMSGDATASTATUS = _descriptor.EnumDescriptor(
    name="ImuMsgDataStatus",
    full_name="apollo.localization.ImuMsgDataStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="IMU_DATA_NORMAL",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_DATA_ABNORMAL",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMU_DATA_OTHER",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=2322,
    serialized_end=2404,
)
_sym_db.RegisterEnumDescriptor(_IMUMSGDATASTATUS)
ImuMsgDataStatus = enum_type_wrapper.EnumTypeWrapper(_IMUMSGDATASTATUS)
_MSFRUNNINGSTATUS = _descriptor.EnumDescriptor(
    name="MsfRunningStatus",
    full_name="apollo.localization.MsfRunningStatus",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_LIDAR_GNSS",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_X_GNSS",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_LIDAR_X",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_LIDAR_XX",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_LIDAR_XXX",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_X_X",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_X_XX",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SOL_X_XXX",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_LIDAR_GNSS",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_X_GNSS",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_LIDAR_X",
            index=10,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_LIDAR_XX",
            index=11,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_LIDAR_XXX",
            index=12,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_X_X",
            index=13,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_X_XX",
            index=14,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_SSOL_X_XXX",
            index=15,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_LIDAR_GNSS",
            index=16,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_X_GNSS",
            index=17,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_LIDAR_X",
            index=18,
            number=18,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_LIDAR_XX",
            index=19,
            number=19,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_LIDAR_XXX",
            index=20,
            number=20,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_X_X",
            index=21,
            number=21,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_X_XX",
            index=22,
            number=22,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_NOSOL_X_XXX",
            index=23,
            number=23,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MSF_RUNNING_INIT",
            index=24,
            number=24,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=2407,
    serialized_end=2963,
)
_sym_db.RegisterEnumDescriptor(_MSFRUNNINGSTATUS)
MsfRunningStatus = enum_type_wrapper.EnumTypeWrapper(_MSFRUNNINGSTATUS)
MSF_LOCAL_LIDAR_NORMAL = 0
MSF_LOCAL_LIDAR_MAP_MISSING = 1
MSF_LOCAL_LIDAR_EXTRINSICS_MISSING = 2
MSF_LOCAL_LIDAR_MAP_LOADING_FAILED = 3
MSF_LOCAL_LIDAR_NO_OUTPUT = 4
MSF_LOCAL_LIDAR_OUT_OF_MAP = 5
MSF_LOCAL_LIDAR_NOT_GOOD = 6
MSF_LOCAL_LIDAR_UNDEFINED_STATUS = 7
MSF_LOCAL_LIDAR_VERY_GOOD = 0
MSF_LOCAL_LIDAR_GOOD = 1
MSF_LOCAL_LIDAR_NOT_BAD = 2
MSF_LOCAL_LIDAR_BAD = 3
MSF_LOCAL_LIDAR_CONSISTENCY_00 = 0
MSF_LOCAL_LIDAR_CONSISTENCY_01 = 1
MSF_LOCAL_LIDAR_CONSISTENCY_02 = 2
MSF_LOCAL_LIDAR_CONSISTENCY_03 = 3
MSF_GNSS_CONSISTENCY_00 = 0
MSF_GNSS_CONSISTENCY_01 = 1
MSF_GNSS_CONSISTENCY_02 = 2
MSF_GNSS_CONSISTENCY_03 = 3
NONE = 0
FIXEDPOS = 1
FIXEDHEIGHT = 2
FLOATCONV = 4
WIDELANE = 5
NARROWLANE = 6
DOPPLER_VELOCITY = 8
SINGLE = 16
PSRDIFF = 17
WAAS = 18
PROPOGATED = 19
OMNISTAR = 20
L1_FLOAT = 32
IONOFREE_FLOAT = 33
NARROW_FLOAT = 34
L1_INT = 48
WIDE_INT = 49
NARROW_INT = 50
RTK_DIRECT_INS = 51
INS_SBAS = 52
INS_PSRSP = 53
INS_PSRDIFF = 54
INS_RTKFLOAT = 55
INS_RTKFIXED = 56
INS_OMNISTAR = 57
INS_OMNISTAR_HP = 58
INS_OMNISTAR_XP = 59
OMNISTAR_HP = 64
OMNISTAR_XP = 65
PPP_CONVERGING = 68
PPP = 69
INS_PPP_Converging = 73
INS_PPP = 74
MSG_LOSS = 91
IMU_DELAY_NORMAL = 0
IMU_DELAY_1 = 1
IMU_DELAY_2 = 2
IMU_DELAY_3 = 3
IMU_DELAY_ABNORMAL = 4
IMU_MISSING_NORMAL = 0
IMU_MISSING_1 = 1
IMU_MISSING_2 = 2
IMU_MISSING_3 = 3
IMU_MISSING_4 = 4
IMU_MISSING_5 = 5
IMU_MISSING_ABNORMAL = 6
IMU_DATA_NORMAL = 0
IMU_DATA_ABNORMAL = 1
IMU_DATA_OTHER = 2
MSF_SOL_LIDAR_GNSS = 0
MSF_SOL_X_GNSS = 1
MSF_SOL_LIDAR_X = 2
MSF_SOL_LIDAR_XX = 3
MSF_SOL_LIDAR_XXX = 4
MSF_SOL_X_X = 5
MSF_SOL_X_XX = 6
MSF_SOL_X_XXX = 7
MSF_SSOL_LIDAR_GNSS = 8
MSF_SSOL_X_GNSS = 9
MSF_SSOL_LIDAR_X = 10
MSF_SSOL_LIDAR_XX = 11
MSF_SSOL_LIDAR_XXX = 12
MSF_SSOL_X_X = 13
MSF_SSOL_X_XX = 14
MSF_SSOL_X_XXX = 15
MSF_NOSOL_LIDAR_GNSS = 16
MSF_NOSOL_X_GNSS = 17
MSF_NOSOL_LIDAR_X = 18
MSF_NOSOL_LIDAR_XX = 19
MSF_NOSOL_LIDAR_XXX = 20
MSF_NOSOL_X_X = 21
MSF_NOSOL_X_XX = 22
MSF_NOSOL_X_XXX = 23
MSF_RUNNING_INIT = 24
_MSFSENSORMSGSTATUS = _descriptor.Descriptor(
    name="MsfSensorMsgStatus",
    full_name="apollo.localization.MsfSensorMsgStatus",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="imu_delay_status",
            full_name="apollo.localization.MsfSensorMsgStatus.imu_delay_status",
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
            name="imu_missing_status",
            full_name="apollo.localization.MsfSensorMsgStatus.imu_missing_status",
            index=1,
            number=2,
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
            name="imu_data_status",
            full_name="apollo.localization.MsfSensorMsgStatus.imu_data_status",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=89,
    serialized_end=309,
)
_MSFSTATUS = _descriptor.Descriptor(
    name="MsfStatus",
    full_name="apollo.localization.MsfStatus",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="local_lidar_consistency",
            full_name="apollo.localization.MsfStatus.local_lidar_consistency",
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
            name="gnss_consistency",
            full_name="apollo.localization.MsfStatus.gnss_consistency",
            index=1,
            number=2,
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
            name="local_lidar_status",
            full_name="apollo.localization.MsfStatus.local_lidar_status",
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
            name="local_lidar_quality",
            full_name="apollo.localization.MsfStatus.local_lidar_quality",
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
        _descriptor.FieldDescriptor(
            name="gnsspos_position_type",
            full_name="apollo.localization.MsfStatus.gnsspos_position_type",
            index=4,
            number=5,
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
            name="msf_running_status",
            full_name="apollo.localization.MsfStatus.msf_running_status",
            index=5,
            number=6,
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
    serialized_start=312,
    serialized_end=737,
)
_MSFSENSORMSGSTATUS.fields_by_name["imu_delay_status"].enum_type = _IMUMSGDELAYSTATUS
_MSFSENSORMSGSTATUS.fields_by_name[
    "imu_missing_status"
].enum_type = _IMUMSGMISSINGSTATUS
_MSFSENSORMSGSTATUS.fields_by_name["imu_data_status"].enum_type = _IMUMSGDATASTATUS
_MSFSTATUS.fields_by_name["local_lidar_consistency"].enum_type = _LOCALLIDARCONSISTENCY
_MSFSTATUS.fields_by_name["gnss_consistency"].enum_type = _GNSSCONSISTENCY
_MSFSTATUS.fields_by_name["local_lidar_status"].enum_type = _LOCALLIDARSTATUS
_MSFSTATUS.fields_by_name["local_lidar_quality"].enum_type = _LOCALLIDARQUALITY
_MSFSTATUS.fields_by_name["gnsspos_position_type"].enum_type = _GNSSPOSITIONTYPE
_MSFSTATUS.fields_by_name["msf_running_status"].enum_type = _MSFRUNNINGSTATUS
DESCRIPTOR.message_types_by_name["MsfSensorMsgStatus"] = _MSFSENSORMSGSTATUS
DESCRIPTOR.message_types_by_name["MsfStatus"] = _MSFSTATUS
DESCRIPTOR.enum_types_by_name["LocalLidarStatus"] = _LOCALLIDARSTATUS
DESCRIPTOR.enum_types_by_name["LocalLidarQuality"] = _LOCALLIDARQUALITY
DESCRIPTOR.enum_types_by_name["LocalLidarConsistency"] = _LOCALLIDARCONSISTENCY
DESCRIPTOR.enum_types_by_name["GnssConsistency"] = _GNSSCONSISTENCY
DESCRIPTOR.enum_types_by_name["GnssPositionType"] = _GNSSPOSITIONTYPE
DESCRIPTOR.enum_types_by_name["ImuMsgDelayStatus"] = _IMUMSGDELAYSTATUS
DESCRIPTOR.enum_types_by_name["ImuMsgMissingStatus"] = _IMUMSGMISSINGSTATUS
DESCRIPTOR.enum_types_by_name["ImuMsgDataStatus"] = _IMUMSGDATASTATUS
DESCRIPTOR.enum_types_by_name["MsfRunningStatus"] = _MSFRUNNINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
MsfSensorMsgStatus = _reflection.GeneratedProtocolMessageType(
    "MsfSensorMsgStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSFSENSORMSGSTATUS,
        "__module__": "modules.common_msgs.localization_msgs.localization_status_pb2",
    },
)
_sym_db.RegisterMessage(MsfSensorMsgStatus)
MsfStatus = _reflection.GeneratedProtocolMessageType(
    "MsfStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSFSTATUS,
        "__module__": "modules.common_msgs.localization_msgs.localization_status_pb2",
    },
)
_sym_db.RegisterMessage(MsfStatus)
