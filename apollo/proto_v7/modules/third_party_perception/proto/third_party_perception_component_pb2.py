"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/third_party_perception/proto/third_party_perception_component.proto",
    package="apollo.third_party_perception",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nKmodules/third_party_perception/proto/third_party_perception_component.proto\x12\x1dapollo.third_party_perception"p\n\x1aThirdPartyPerceptionDevice\x12R\n\x0bdevice_type\x18\x01 \x01(\x0e2=.apollo.third_party_perception.ThirdPartyPerceptionDeviceType*>\n\x1eThirdPartyPerceptionDeviceType\x12\x0e\n\nSMARTEREYE\x10\x00\x12\x0c\n\x08MOBILEYE\x10\x01',
)
_THIRDPARTYPERCEPTIONDEVICETYPE = _descriptor.EnumDescriptor(
    name="ThirdPartyPerceptionDeviceType",
    full_name="apollo.third_party_perception.ThirdPartyPerceptionDeviceType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SMARTEREYE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MOBILEYE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=224,
    serialized_end=286,
)
_sym_db.RegisterEnumDescriptor(_THIRDPARTYPERCEPTIONDEVICETYPE)
ThirdPartyPerceptionDeviceType = enum_type_wrapper.EnumTypeWrapper(
    _THIRDPARTYPERCEPTIONDEVICETYPE
)
SMARTEREYE = 0
MOBILEYE = 1
_THIRDPARTYPERCEPTIONDEVICE = _descriptor.Descriptor(
    name="ThirdPartyPerceptionDevice",
    full_name="apollo.third_party_perception.ThirdPartyPerceptionDevice",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="device_type",
            full_name="apollo.third_party_perception.ThirdPartyPerceptionDevice.device_type",
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
    serialized_start=110,
    serialized_end=222,
)
_THIRDPARTYPERCEPTIONDEVICE.fields_by_name[
    "device_type"
].enum_type = _THIRDPARTYPERCEPTIONDEVICETYPE
DESCRIPTOR.message_types_by_name[
    "ThirdPartyPerceptionDevice"
] = _THIRDPARTYPERCEPTIONDEVICE
DESCRIPTOR.enum_types_by_name[
    "ThirdPartyPerceptionDeviceType"
] = _THIRDPARTYPERCEPTIONDEVICETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ThirdPartyPerceptionDevice = _reflection.GeneratedProtocolMessageType(
    "ThirdPartyPerceptionDevice",
    (_message.Message,),
    {
        "DESCRIPTOR": _THIRDPARTYPERCEPTIONDEVICE,
        "__module__": "modules.third_party_perception.proto.third_party_perception_component_pb2",
    },
)
_sym_db.RegisterMessage(ThirdPartyPerceptionDevice)
