"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.map_msgs import (
    map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2,
)
from ....modules.common_msgs.map_msgs import (
    map_id_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/map_msgs/map_crosswalk.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n0modules/common_msgs/map_msgs/map_crosswalk.proto\x12\x0capollo.hdmap\x1a/modules/common_msgs/map_msgs/map_geometry.proto\x1a)modules/common_msgs/map_msgs/map_id.proto"w\n\tCrosswalk\x12\x1c\n\x02id\x18\x01 \x01(\x0b2\x10.apollo.hdmap.Id\x12&\n\x07polygon\x18\x02 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x03 \x03(\x0b2\x10.apollo.hdmap.Id',
    dependencies=[
        modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2.DESCRIPTOR,
    ],
)
_CROSSWALK = _descriptor.Descriptor(
    name="Crosswalk",
    full_name="apollo.hdmap.Crosswalk",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="apollo.hdmap.Crosswalk.id",
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
            name="polygon",
            full_name="apollo.hdmap.Crosswalk.polygon",
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
            name="overlap_id",
            full_name="apollo.hdmap.Crosswalk.overlap_id",
            index=2,
            number=3,
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
    serialized_start=158,
    serialized_end=277,
)
_CROSSWALK.fields_by_name[
    "id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
_CROSSWALK.fields_by_name[
    "polygon"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2._POLYGON
_CROSSWALK.fields_by_name[
    "overlap_id"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2._ID
DESCRIPTOR.message_types_by_name["Crosswalk"] = _CROSSWALK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
Crosswalk = _reflection.GeneratedProtocolMessageType(
    "Crosswalk",
    (_message.Message,),
    {
        "DESCRIPTOR": _CROSSWALK,
        "__module__": "modules.common_msgs.map_msgs.map_crosswalk_pb2",
    },
)
_sym_db.RegisterMessage(Crosswalk)
