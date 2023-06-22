"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/proto/roi_boundary_filter_config.proto",
    package="apollo.perception.lidar",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n9modules/perception/proto/roi_boundary_filter_config.proto\x12\x17apollo.perception.lidar"\xa6\x01\n\x17ROIBoundaryFilterConfig\x12)\n\x1edistance_to_boundary_threshold\x18\x01 \x01(\x01:\x011\x12!\n\x14confidence_threshold\x18\x02 \x01(\x02:\x030.5\x12 \n\x13cross_roi_threshold\x18\x03 \x01(\x02:\x030.6\x12\x1b\n\x10inside_threshold\x18\x04 \x01(\x01:\x011',
)
_ROIBOUNDARYFILTERCONFIG = _descriptor.Descriptor(
    name="ROIBoundaryFilterConfig",
    full_name="apollo.perception.lidar.ROIBoundaryFilterConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="distance_to_boundary_threshold",
            full_name="apollo.perception.lidar.ROIBoundaryFilterConfig.distance_to_boundary_threshold",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(1),
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
            name="confidence_threshold",
            full_name="apollo.perception.lidar.ROIBoundaryFilterConfig.confidence_threshold",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=True,
            default_value=float(0.5),
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
            name="cross_roi_threshold",
            full_name="apollo.perception.lidar.ROIBoundaryFilterConfig.cross_roi_threshold",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=True,
            default_value=float(0.6),
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
            name="inside_threshold",
            full_name="apollo.perception.lidar.ROIBoundaryFilterConfig.inside_threshold",
            index=3,
            number=4,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(1),
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
    serialized_start=87,
    serialized_end=253,
)
DESCRIPTOR.message_types_by_name["ROIBoundaryFilterConfig"] = _ROIBOUNDARYFILTERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ROIBoundaryFilterConfig = _reflection.GeneratedProtocolMessageType(
    "ROIBoundaryFilterConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROIBOUNDARYFILTERCONFIG,
        "__module__": "modules.perception.proto.roi_boundary_filter_config_pb2",
    },
)
_sym_db.RegisterMessage(ROIBoundaryFilterConfig)
