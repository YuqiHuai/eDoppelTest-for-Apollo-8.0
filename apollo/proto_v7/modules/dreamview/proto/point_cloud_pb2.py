"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/dreamview/proto/point_cloud.proto",
    package="apollo.dreamview",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n)modules/dreamview/proto/point_cloud.proto\x12\x10apollo.dreamview"\x1d\n\nPointCloud\x12\x0f\n\x03num\x18\x01 \x03(\x02B\x02\x10\x01',
)
_POINTCLOUD = _descriptor.Descriptor(
    name="PointCloud",
    full_name="apollo.dreamview.PointCloud",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="num",
            full_name="apollo.dreamview.PointCloud.num",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
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
    serialized_start=63,
    serialized_end=92,
)
DESCRIPTOR.message_types_by_name["PointCloud"] = _POINTCLOUD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PointCloud = _reflection.GeneratedProtocolMessageType(
    "PointCloud",
    (_message.Message,),
    {
        "DESCRIPTOR": _POINTCLOUD,
        "__module__": "modules.dreamview.proto.point_cloud_pb2",
    },
)
_sym_db.RegisterMessage(PointCloud)
_POINTCLOUD.fields_by_name["num"]._options = None
