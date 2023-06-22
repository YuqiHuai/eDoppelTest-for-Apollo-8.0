"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/onboard/proto/fusion_camera_detection_component.proto",
    package="apollo.perception.onboard",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nHmodules/perception/onboard/proto/fusion_camera_detection_component.proto\x12\x19apollo.perception.onboard"\xc9\x0b\n\x15FusionCameraDetection\x12*\n\x0ccamera_names\x18\x01 \x01(\t:\x14front_6mm,front_12mm\x12k\n\x1ainput_camera_channel_names\x18\x02 \x01(\t:G/sensor/camera/traffic/image_short,/sensor/camera/obstacle/image_narrow\x12\x1b\n\x10timestamp_offset\x18\x03 \x01(\x01:\x010\x12C\n#camera_obstacle_perception_conf_dir\x18\x04 \x01(\t:\x16conf/perception/camera\x129\n$camera_obstacle_perception_conf_file\x18\x05 \x01(\t:\x0bobstacle.pt\x12\x1a\n\x0eframe_capacity\x18\x06 \x01(\x05:\x0220\x12\x1c\n\x11image_channel_num\x18\x07 \x01(\x05:\x013\x12"\n\x13enable_undistortion\x18\x08 \x01(\x08:\x05false\x12#\n\x14enable_visualization\x18\t \x01(\x08:\x05false\x12<\n\x1doutput_obstacles_channel_name\x18\n \x01(\t:\x15/perception/obstacles\x12T\n*camera_perception_viz_message_channel_name\x18\x0b \x01(\t: /perception/inner/camera_viz_msg\x12@\n\x15prefused_channel_name\x18\x0c \x01(\t:!/perception/inner/PrefusedObjects\x12\x1f\n\x14default_camera_pitch\x18\r \x01(\x01:\x010\x12"\n\x15default_camera_height\x18\x0e \x01(\x01:\x031.5\x127\n$lane_calibration_working_sensor_name\x18\x0f \x01(\t:\tfront_6mm\x12-\n\x11calibrator_method\x18\x10 \x01(\t:\x12LaneLineCalibrator\x124\n\x12calib_service_name\x18\x11 \x01(\t:\x18OnlineCalibrationService\x12\x1f\n\x11run_calib_service\x18\x12 \x01(\x08:\x04true\x12&\n\x17output_camera_debug_msg\x18\x13 \x01(\x08:\x05false\x12;\n\x19camera_debug_channel_name\x18\x14 \x01(\t:\x18/perception/camera_debug\x12\x14\n\x07ts_diff\x18\x15 \x01(\x01:\x030.1\x12%\n\x16output_final_obstacles\x18\x16 \x01(\x08:\x05false\x121\n\x13visual_debug_folder\x18\x17 \x01(\t:\x14/apollo/debug_output\x12 \n\rvisual_camera\x18\x18 \x01(\t:\tfront_6mm\x12\x1f\n\x10write_visual_img\x18\x19 \x01(\x08:\x05false\x12\'\n\x1cmin_laneline_length_for_cipv\x18\x1a \x01(\x01:\x012\x12(\n\x1baverage_lane_width_in_meter\x18\x1b \x01(\x01:\x033.7\x12\'\n\x1amax_vehicle_width_in_meter\x18\x1c \x01(\x01:\x032.5\x12 \n\x12average_frame_rate\x18\x1d \x01(\x01:\x040.05\x12\x1f\n\x10image_based_cipv\x18\x1e \x01(\x08:\x05false\x12\x16\n\x0bdebug_level\x18\x1f \x01(\x05:\x010\x12\x1a\n\x0benable_cipv\x18  \x01(\x08:\x05false\x12\x12\n\x04cipv\x18! \x01(\t:\x04Cipv',
)
_FUSIONCAMERADETECTION = _descriptor.Descriptor(
    name="FusionCameraDetection",
    full_name="apollo.perception.onboard.FusionCameraDetection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="camera_names",
            full_name="apollo.perception.onboard.FusionCameraDetection.camera_names",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"front_6mm,front_12mm".decode("utf-8"),
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
            name="input_camera_channel_names",
            full_name="apollo.perception.onboard.FusionCameraDetection.input_camera_channel_names",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"/sensor/camera/traffic/image_short,/sensor/camera/obstacle/image_narrow".decode(
                "utf-8"
            ),
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
            name="timestamp_offset",
            full_name="apollo.perception.onboard.FusionCameraDetection.timestamp_offset",
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
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
            name="camera_obstacle_perception_conf_dir",
            full_name="apollo.perception.onboard.FusionCameraDetection.camera_obstacle_perception_conf_dir",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"conf/perception/camera".decode("utf-8"),
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
            name="camera_obstacle_perception_conf_file",
            full_name="apollo.perception.onboard.FusionCameraDetection.camera_obstacle_perception_conf_file",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"obstacle.pt".decode("utf-8"),
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
            name="frame_capacity",
            full_name="apollo.perception.onboard.FusionCameraDetection.frame_capacity",
            index=5,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=True,
            default_value=20,
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
            name="image_channel_num",
            full_name="apollo.perception.onboard.FusionCameraDetection.image_channel_num",
            index=6,
            number=7,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=True,
            default_value=3,
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
            name="enable_undistortion",
            full_name="apollo.perception.onboard.FusionCameraDetection.enable_undistortion",
            index=7,
            number=8,
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
            name="enable_visualization",
            full_name="apollo.perception.onboard.FusionCameraDetection.enable_visualization",
            index=8,
            number=9,
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
            name="output_obstacles_channel_name",
            full_name="apollo.perception.onboard.FusionCameraDetection.output_obstacles_channel_name",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"/perception/obstacles".decode("utf-8"),
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
            name="camera_perception_viz_message_channel_name",
            full_name="apollo.perception.onboard.FusionCameraDetection.camera_perception_viz_message_channel_name",
            index=10,
            number=11,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"/perception/inner/camera_viz_msg".decode("utf-8"),
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
            name="prefused_channel_name",
            full_name="apollo.perception.onboard.FusionCameraDetection.prefused_channel_name",
            index=11,
            number=12,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"/perception/inner/PrefusedObjects".decode("utf-8"),
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
            name="default_camera_pitch",
            full_name="apollo.perception.onboard.FusionCameraDetection.default_camera_pitch",
            index=12,
            number=13,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
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
            name="default_camera_height",
            full_name="apollo.perception.onboard.FusionCameraDetection.default_camera_height",
            index=13,
            number=14,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(1.5),
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
            name="lane_calibration_working_sensor_name",
            full_name="apollo.perception.onboard.FusionCameraDetection.lane_calibration_working_sensor_name",
            index=14,
            number=15,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"front_6mm".decode("utf-8"),
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
            name="calibrator_method",
            full_name="apollo.perception.onboard.FusionCameraDetection.calibrator_method",
            index=15,
            number=16,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"LaneLineCalibrator".decode("utf-8"),
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
            name="calib_service_name",
            full_name="apollo.perception.onboard.FusionCameraDetection.calib_service_name",
            index=16,
            number=17,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"OnlineCalibrationService".decode("utf-8"),
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
            name="run_calib_service",
            full_name="apollo.perception.onboard.FusionCameraDetection.run_calib_service",
            index=17,
            number=18,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=True,
            default_value=True,
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
            name="output_camera_debug_msg",
            full_name="apollo.perception.onboard.FusionCameraDetection.output_camera_debug_msg",
            index=18,
            number=19,
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
            name="camera_debug_channel_name",
            full_name="apollo.perception.onboard.FusionCameraDetection.camera_debug_channel_name",
            index=19,
            number=20,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"/perception/camera_debug".decode("utf-8"),
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
            name="ts_diff",
            full_name="apollo.perception.onboard.FusionCameraDetection.ts_diff",
            index=20,
            number=21,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(0.1),
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
            name="output_final_obstacles",
            full_name="apollo.perception.onboard.FusionCameraDetection.output_final_obstacles",
            index=21,
            number=22,
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
            name="visual_debug_folder",
            full_name="apollo.perception.onboard.FusionCameraDetection.visual_debug_folder",
            index=22,
            number=23,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"/apollo/debug_output".decode("utf-8"),
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
            name="visual_camera",
            full_name="apollo.perception.onboard.FusionCameraDetection.visual_camera",
            index=23,
            number=24,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"front_6mm".decode("utf-8"),
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
            name="write_visual_img",
            full_name="apollo.perception.onboard.FusionCameraDetection.write_visual_img",
            index=24,
            number=25,
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
            name="min_laneline_length_for_cipv",
            full_name="apollo.perception.onboard.FusionCameraDetection.min_laneline_length_for_cipv",
            index=25,
            number=26,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(2),
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
            name="average_lane_width_in_meter",
            full_name="apollo.perception.onboard.FusionCameraDetection.average_lane_width_in_meter",
            index=26,
            number=27,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(3.7),
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
            name="max_vehicle_width_in_meter",
            full_name="apollo.perception.onboard.FusionCameraDetection.max_vehicle_width_in_meter",
            index=27,
            number=28,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(2.5),
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
            name="average_frame_rate",
            full_name="apollo.perception.onboard.FusionCameraDetection.average_frame_rate",
            index=28,
            number=29,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=True,
            default_value=float(0.05),
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
            name="image_based_cipv",
            full_name="apollo.perception.onboard.FusionCameraDetection.image_based_cipv",
            index=29,
            number=30,
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
            name="debug_level",
            full_name="apollo.perception.onboard.FusionCameraDetection.debug_level",
            index=30,
            number=31,
            type=5,
            cpp_type=1,
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
            name="enable_cipv",
            full_name="apollo.perception.onboard.FusionCameraDetection.enable_cipv",
            index=31,
            number=32,
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
            name="cipv",
            full_name="apollo.perception.onboard.FusionCameraDetection.cipv",
            index=32,
            number=33,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
            default_value=b"Cipv".decode("utf-8"),
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
    serialized_start=104,
    serialized_end=1585,
)
DESCRIPTOR.message_types_by_name["FusionCameraDetection"] = _FUSIONCAMERADETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
FusionCameraDetection = _reflection.GeneratedProtocolMessageType(
    "FusionCameraDetection",
    (_message.Message,),
    {
        "DESCRIPTOR": _FUSIONCAMERADETECTION,
        "__module__": "modules.perception.onboard.proto.fusion_camera_detection_component_pb2",
    },
)
_sym_db.RegisterMessage(FusionCameraDetection)
