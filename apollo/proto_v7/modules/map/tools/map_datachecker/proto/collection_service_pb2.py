"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
from ......modules.map.tools.map_datachecker.proto import (
    collection_check_message_pb2 as modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/map/tools/map_datachecker/proto/collection_service.proto",
    package="apollo.hdmap",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n@modules/map/tools/map_datachecker/proto/collection_service.proto\x12\x0capollo.hdmap\x1aFmodules/map/tools/map_datachecker/proto/collection_check_message.proto2\xf1\x03\n\x18CollectionCheckerService\x12^\n\x13ServiceDynamicAlign\x12!.apollo.hdmap.DynamicAlignRequest\x1a".apollo.hdmap.DynamicAlignResponse"\x00\x12[\n\x12ServiceStaticAlign\x12 .apollo.hdmap.StaticAlignRequest\x1a!.apollo.hdmap.StaticAlignResponse"\x00\x12X\n\x11ServiceEightRoute\x12\x1f.apollo.hdmap.EightRouteRequest\x1a .apollo.hdmap.EightRouteResponse"\x00\x12a\n\x14ServiceChannelVerify\x12".apollo.hdmap.ChannelVerifyRequest\x1a#.apollo.hdmap.ChannelVerifyResponse"\x00\x12[\n\x12ServiceLoopsVerify\x12 .apollo.hdmap.LoopsVerifyRequest\x1a!.apollo.hdmap.LoopsVerifyResponse"\x00',
    dependencies=[
        modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2.DESCRIPTOR
    ],
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
_COLLECTIONCHECKERSERVICE = _descriptor.ServiceDescriptor(
    name="CollectionCheckerService",
    full_name="apollo.hdmap.CollectionCheckerService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=155,
    serialized_end=652,
    methods=[
        _descriptor.MethodDescriptor(
            name="ServiceDynamicAlign",
            full_name="apollo.hdmap.CollectionCheckerService.ServiceDynamicAlign",
            index=0,
            containing_service=None,
            input_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._DYNAMICALIGNREQUEST,
            output_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._DYNAMICALIGNRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ServiceStaticAlign",
            full_name="apollo.hdmap.CollectionCheckerService.ServiceStaticAlign",
            index=1,
            containing_service=None,
            input_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._STATICALIGNREQUEST,
            output_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._STATICALIGNRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ServiceEightRoute",
            full_name="apollo.hdmap.CollectionCheckerService.ServiceEightRoute",
            index=2,
            containing_service=None,
            input_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._EIGHTROUTEREQUEST,
            output_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._EIGHTROUTERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ServiceChannelVerify",
            full_name="apollo.hdmap.CollectionCheckerService.ServiceChannelVerify",
            index=3,
            containing_service=None,
            input_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._CHANNELVERIFYREQUEST,
            output_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._CHANNELVERIFYRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ServiceLoopsVerify",
            full_name="apollo.hdmap.CollectionCheckerService.ServiceLoopsVerify",
            index=4,
            containing_service=None,
            input_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._LOOPSVERIFYREQUEST,
            output_type=modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2._LOOPSVERIFYRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_COLLECTIONCHECKERSERVICE)
DESCRIPTOR.services_by_name["CollectionCheckerService"] = _COLLECTIONCHECKERSERVICE
