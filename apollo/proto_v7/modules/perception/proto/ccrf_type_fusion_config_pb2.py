"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/perception/proto/ccrf_type_fusion_config.proto",
    package="apollo.perception.lidar",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n6modules/perception/proto/ccrf_type_fusion_config.proto\x12\x17apollo.perception.lidar\"\x8f\x01\n\x14CcrfTypeFusionConfig\x12(\n\x1eclassifiers_property_file_path\x18\x01 \x01(\t:\x00\x12'\n\x1dtransition_property_file_path\x18\x02 \x01(\t:\x00\x12$\n\x17transition_matrix_alpha\x18\x03 \x01(\x02:\x031.8",
)
_CCRFTYPEFUSIONCONFIG = _descriptor.Descriptor(
    name="CcrfTypeFusionConfig",
    full_name="apollo.perception.lidar.CcrfTypeFusionConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="classifiers_property_file_path",
            full_name="apollo.perception.lidar.CcrfTypeFusionConfig.classifiers_property_file_path",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
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
            name="transition_property_file_path",
            full_name="apollo.perception.lidar.CcrfTypeFusionConfig.transition_property_file_path",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=True,
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
            name="transition_matrix_alpha",
            full_name="apollo.perception.lidar.CcrfTypeFusionConfig.transition_matrix_alpha",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=True,
            default_value=float(1.8),
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
    serialized_start=84,
    serialized_end=227,
)
DESCRIPTOR.message_types_by_name["CcrfTypeFusionConfig"] = _CCRFTYPEFUSIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CcrfTypeFusionConfig = _reflection.GeneratedProtocolMessageType(
    "CcrfTypeFusionConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _CCRFTYPEFUSIONCONFIG,
        "__module__": "modules.perception.proto.ccrf_type_fusion_config_pb2",
    },
)
_sym_db.RegisterMessage(CcrfTypeFusionConfig)
