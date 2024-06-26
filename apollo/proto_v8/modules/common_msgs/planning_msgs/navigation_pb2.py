"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)
from ....modules.common_msgs.basic_msgs import (
    pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2,
)
from ....modules.common_msgs.localization_msgs import (
    localization_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_localization__pb2,
)
from ....modules.common_msgs.map_msgs import (
    map_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__pb2,
)
from ....modules.common_msgs.perception_msgs import (
    perception_obstacle_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/planning_msgs/navigation.proto",
    package="apollo.relative_map",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n2modules/common_msgs/planning_msgs/navigation.proto\x12\x13apollo.relative_map\x1a+modules/common_msgs/basic_msgs/header.proto\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a8modules/common_msgs/localization_msgs/localization.proto\x1a&modules/common_msgs/map_msgs/map.proto\x1a=modules/common_msgs/perception_msgs/perception_obstacle.proto"J\n\x0eNavigationPath\x12!\n\x04path\x18\x01 \x01(\x0b2\x13.apollo.common.Path\x12\x15\n\rpath_priority\x18\x02 \x01(\r"u\n\x0eNavigationInfo\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12<\n\x0fnavigation_path\x18\x02 \x03(\x0b2#.apollo.relative_map.NavigationPath"\xed\x02\n\x06MapMsg\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12 \n\x05hdmap\x18\x02 \x01(\x0b2\x11.apollo.hdmap.Map\x12H\n\x0fnavigation_path\x18\x03 \x03(\x0b2/.apollo.relative_map.MapMsg.NavigationPathEntry\x123\n\x0blane_marker\x18\x04 \x01(\x0b2\x1e.apollo.perception.LaneMarkers\x12?\n\x0clocalization\x18\x05 \x01(\x0b2).apollo.localization.LocalizationEstimate\x1aZ\n\x13NavigationPathEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x122\n\x05value\x18\x02 \x01(\x0b2#.apollo.relative_map.NavigationPath:\x028\x01',
    dependencies=[
        modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_localization__msgs_dot_localization__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_map__msgs_dot_map__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2.DESCRIPTOR,
    ],
)
_NAVIGATIONPATH = _descriptor.Descriptor(
    name="NavigationPath",
    full_name="apollo.relative_map.NavigationPath",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="path",
            full_name="apollo.relative_map.NavigationPath.path",
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
            name="path_priority",
            full_name="apollo.relative_map.NavigationPath.path_priority",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
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
    serialized_start=329,
    serialized_end=403,
)
_NAVIGATIONINFO = _descriptor.Descriptor(
    name="NavigationInfo",
    full_name="apollo.relative_map.NavigationInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.relative_map.NavigationInfo.header",
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
            name="navigation_path",
            full_name="apollo.relative_map.NavigationInfo.navigation_path",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=405,
    serialized_end=522,
)
_MAPMSG_NAVIGATIONPATHENTRY = _descriptor.Descriptor(
    name="NavigationPathEntry",
    full_name="apollo.relative_map.MapMsg.NavigationPathEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="apollo.relative_map.MapMsg.NavigationPathEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
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
            name="value",
            full_name="apollo.relative_map.MapMsg.NavigationPathEntry.value",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\x01",
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=800,
    serialized_end=890,
)
_MAPMSG = _descriptor.Descriptor(
    name="MapMsg",
    full_name="apollo.relative_map.MapMsg",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.relative_map.MapMsg.header",
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
            name="hdmap",
            full_name="apollo.relative_map.MapMsg.hdmap",
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
            name="navigation_path",
            full_name="apollo.relative_map.MapMsg.navigation_path",
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
        _descriptor.FieldDescriptor(
            name="lane_marker",
            full_name="apollo.relative_map.MapMsg.lane_marker",
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
            name="localization",
            full_name="apollo.relative_map.MapMsg.localization",
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
    ],
    extensions=[],
    nested_types=[_MAPMSG_NAVIGATIONPATHENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=525,
    serialized_end=890,
)
_NAVIGATIONPATH.fields_by_name[
    "path"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2._PATH
_NAVIGATIONINFO.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_NAVIGATIONINFO.fields_by_name["navigation_path"].message_type = _NAVIGATIONPATH
_MAPMSG_NAVIGATIONPATHENTRY.fields_by_name["value"].message_type = _NAVIGATIONPATH
_MAPMSG_NAVIGATIONPATHENTRY.containing_type = _MAPMSG
_MAPMSG.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_MAPMSG.fields_by_name[
    "hdmap"
].message_type = modules_dot_common__msgs_dot_map__msgs_dot_map__pb2._MAP
_MAPMSG.fields_by_name["navigation_path"].message_type = _MAPMSG_NAVIGATIONPATHENTRY
_MAPMSG.fields_by_name[
    "lane_marker"
].message_type = (
    modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2._LANEMARKERS
)
_MAPMSG.fields_by_name[
    "localization"
].message_type = (
    modules_dot_common__msgs_dot_localization__msgs_dot_localization__pb2._LOCALIZATIONESTIMATE
)
DESCRIPTOR.message_types_by_name["NavigationPath"] = _NAVIGATIONPATH
DESCRIPTOR.message_types_by_name["NavigationInfo"] = _NAVIGATIONINFO
DESCRIPTOR.message_types_by_name["MapMsg"] = _MAPMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
NavigationPath = _reflection.GeneratedProtocolMessageType(
    "NavigationPath",
    (_message.Message,),
    {
        "DESCRIPTOR": _NAVIGATIONPATH,
        "__module__": "modules.common_msgs.planning_msgs.navigation_pb2",
    },
)
_sym_db.RegisterMessage(NavigationPath)
NavigationInfo = _reflection.GeneratedProtocolMessageType(
    "NavigationInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _NAVIGATIONINFO,
        "__module__": "modules.common_msgs.planning_msgs.navigation_pb2",
    },
)
_sym_db.RegisterMessage(NavigationInfo)
MapMsg = _reflection.GeneratedProtocolMessageType(
    "MapMsg",
    (_message.Message,),
    {
        "NavigationPathEntry": _reflection.GeneratedProtocolMessageType(
            "NavigationPathEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _MAPMSG_NAVIGATIONPATHENTRY,
                "__module__": "modules.common_msgs.planning_msgs.navigation_pb2",
            },
        ),
        "DESCRIPTOR": _MAPMSG,
        "__module__": "modules.common_msgs.planning_msgs.navigation_pb2",
    },
)
_sym_db.RegisterMessage(MapMsg)
_sym_db.RegisterMessage(MapMsg.NavigationPathEntry)
_MAPMSG_NAVIGATIONPATHENTRY._options = None
