"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/control/proto/calibration_table.proto",
    package="apollo.control.calibrationtable",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-modules/control/proto/calibration_table.proto\x12\x1fapollo.control.calibrationtable"g\n\x17ControlCalibrationTable\x12L\n\x0bcalibration\x18\x01 \x03(\x0b27.apollo.control.calibrationtable.ControlCalibrationInfo"N\n\x16ControlCalibrationInfo\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x14\n\x0cacceleration\x18\x02 \x01(\x01\x12\x0f\n\x07command\x18\x03 \x01(\x01',
)
_CONTROLCALIBRATIONTABLE = _descriptor.Descriptor(
    name="ControlCalibrationTable",
    full_name="apollo.control.calibrationtable.ControlCalibrationTable",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="calibration",
            full_name="apollo.control.calibrationtable.ControlCalibrationTable.calibration",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=82,
    serialized_end=185,
)
_CONTROLCALIBRATIONINFO = _descriptor.Descriptor(
    name="ControlCalibrationInfo",
    full_name="apollo.control.calibrationtable.ControlCalibrationInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="speed",
            full_name="apollo.control.calibrationtable.ControlCalibrationInfo.speed",
            index=0,
            number=1,
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
            name="acceleration",
            full_name="apollo.control.calibrationtable.ControlCalibrationInfo.acceleration",
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
            name="command",
            full_name="apollo.control.calibrationtable.ControlCalibrationInfo.command",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=187,
    serialized_end=265,
)
_CONTROLCALIBRATIONTABLE.fields_by_name[
    "calibration"
].message_type = _CONTROLCALIBRATIONINFO
DESCRIPTOR.message_types_by_name["ControlCalibrationTable"] = _CONTROLCALIBRATIONTABLE
DESCRIPTOR.message_types_by_name["ControlCalibrationInfo"] = _CONTROLCALIBRATIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ControlCalibrationTable = _reflection.GeneratedProtocolMessageType(
    "ControlCalibrationTable",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTROLCALIBRATIONTABLE,
        "__module__": "modules.control.proto.calibration_table_pb2",
    },
)
_sym_db.RegisterMessage(ControlCalibrationTable)
ControlCalibrationInfo = _reflection.GeneratedProtocolMessageType(
    "ControlCalibrationInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTROLCALIBRATIONINFO,
        "__module__": "modules.control.proto.calibration_table_pb2",
    },
)
_sym_db.RegisterMessage(ControlCalibrationInfo)
