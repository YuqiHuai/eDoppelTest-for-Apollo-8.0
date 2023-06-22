"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common.proto import (
    geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2,
)
from ....modules.common.proto import (
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/localization/proto/sins_pva.proto",
    package="apollo.localization",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n)modules/localization/proto/sins_pva.proto\x12\x13apollo.localization\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto"\xe7\x01\n\x0cIntegSinsPva\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12)\n\x08position\x18\x02 \x01(\x0b2\x17.apollo.common.PointLLH\x12(\n\x08velocity\x18\x03 \x01(\x0b2\x16.apollo.common.Point3D\x12(\n\x08attitude\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12\x15\n\tpva_covar\x18\x05 \x03(\x01B\x02\x10\x01\x12\x1a\n\x12init_and_alignment\x18\x06 \x01(\x08',
    dependencies=[
        modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,
        modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,
    ],
)
_INTEGSINSPVA = _descriptor.Descriptor(
    name="IntegSinsPva",
    full_name="apollo.localization.IntegSinsPva",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.localization.IntegSinsPva.header",
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
            name="position",
            full_name="apollo.localization.IntegSinsPva.position",
            index=1,
            number=2,
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
            name="velocity",
            full_name="apollo.localization.IntegSinsPva.velocity",
            index=2,
            number=3,
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
            name="attitude",
            full_name="apollo.localization.IntegSinsPva.attitude",
            index=3,
            number=4,
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
            name="pva_covar",
            full_name="apollo.localization.IntegSinsPva.pva_covar",
            index=4,
            number=5,
            type=1,
            cpp_type=5,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\x10\x01",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="init_and_alignment",
            full_name="apollo.localization.IntegSinsPva.init_and_alignment",
            index=5,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=139,
    serialized_end=370,
)
_INTEGSINSPVA.fields_by_name[
    "header"
].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INTEGSINSPVA.fields_by_name[
    "position"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINTLLH
_INTEGSINSPVA.fields_by_name[
    "velocity"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INTEGSINSPVA.fields_by_name[
    "attitude"
].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
DESCRIPTOR.message_types_by_name["IntegSinsPva"] = _INTEGSINSPVA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
IntegSinsPva = _reflection.GeneratedProtocolMessageType(
    "IntegSinsPva",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTEGSINSPVA,
        "__module__": "modules.localization.proto.sins_pva_pb2",
    },
)
_sym_db.RegisterMessage(IntegSinsPva)
_INTEGSINSPVA.fields_by_name["pva_covar"]._options = None
