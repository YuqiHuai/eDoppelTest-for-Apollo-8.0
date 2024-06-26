"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import (
    header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2,
)
from ....modules.common_msgs.map_msgs import (
    map_parking_space_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__parking__space__pb2,
)
from ....modules.common_msgs.routing_msgs import (
    routing_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/common_msgs/task_manager_msgs/task_manager.proto",
    package="apollo.task_manager",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n8modules/common_msgs/task_manager_msgs/task_manager.proto\x12\x13apollo.task_manager\x1a+modules/common_msgs/basic_msgs/header.proto\x1a4modules/common_msgs/map_msgs/map_parking_space.proto\x1a.modules/common_msgs/routing_msgs/routing.proto"^\n\x10CycleRoutingTask\x12\x11\n\tcycle_num\x18\x01 \x01(\x05\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"a\n\x12ParkingRoutingTask\x12\x12\n\nlane_width\x18\x01 \x01(\x01\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"_\n\x11ParkGoRoutingTask\x12\x11\n\tpark_time\x18\x01 \x01(\x05\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"\xc2\x02\n\x04Task\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x11\n\ttask_name\x18\x02 \x01(\t\x120\n\ttask_type\x18\x03 \x01(\x0e2\x1d.apollo.task_manager.TaskType\x12A\n\x12cycle_routing_task\x18\x04 \x01(\x0b2%.apollo.task_manager.CycleRoutingTask\x12E\n\x14parking_routing_task\x18\x05 \x01(\x0b2\'.apollo.task_manager.ParkingRoutingTask\x12D\n\x14park_go_routing_task\x18\x06 \x01(\x0b2&.apollo.task_manager.ParkGoRoutingTask*G\n\x08TaskType\x12\x11\n\rCYCLE_ROUTING\x10\x00\x12\x13\n\x0fPARKING_ROUTING\x10\x01\x12\x13\n\x0fPARK_GO_ROUTING\x10\x02*V\n\x0cJunctionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02\x12\r\n\tFORK_ROAD\x10\x03\x12\r\n\tMAIN_SIDE\x10\x04',
    dependencies=[
        modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_map__msgs_dot_map__parking__space__pb2.DESCRIPTOR,
        modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2.DESCRIPTOR,
    ],
)
_TASKTYPE = _descriptor.EnumDescriptor(
    name="TaskType",
    full_name="apollo.task_manager.TaskType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CYCLE_ROUTING",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARKING_ROUTING",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARK_GO_ROUTING",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=845,
    serialized_end=916,
)
_sym_db.RegisterEnumDescriptor(_TASKTYPE)
TaskType = enum_type_wrapper.EnumTypeWrapper(_TASKTYPE)
_JUNCTIONTYPE = _descriptor.EnumDescriptor(
    name="JunctionType",
    full_name="apollo.task_manager.JunctionType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IN_ROAD",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CROSS_ROAD",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FORK_ROAD",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MAIN_SIDE",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=918,
    serialized_end=1004,
)
_sym_db.RegisterEnumDescriptor(_JUNCTIONTYPE)
JunctionType = enum_type_wrapper.EnumTypeWrapper(_JUNCTIONTYPE)
CYCLE_ROUTING = 0
PARKING_ROUTING = 1
PARK_GO_ROUTING = 2
UNKNOWN = 0
IN_ROAD = 1
CROSS_ROAD = 2
FORK_ROAD = 3
MAIN_SIDE = 4
_CYCLEROUTINGTASK = _descriptor.Descriptor(
    name="CycleRoutingTask",
    full_name="apollo.task_manager.CycleRoutingTask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="cycle_num",
            full_name="apollo.task_manager.CycleRoutingTask.cycle_num",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
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
        _descriptor.FieldDescriptor(
            name="routing_request",
            full_name="apollo.task_manager.CycleRoutingTask.routing_request",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=228,
    serialized_end=322,
)
_PARKINGROUTINGTASK = _descriptor.Descriptor(
    name="ParkingRoutingTask",
    full_name="apollo.task_manager.ParkingRoutingTask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="lane_width",
            full_name="apollo.task_manager.ParkingRoutingTask.lane_width",
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
            name="routing_request",
            full_name="apollo.task_manager.ParkingRoutingTask.routing_request",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=324,
    serialized_end=421,
)
_PARKGOROUTINGTASK = _descriptor.Descriptor(
    name="ParkGoRoutingTask",
    full_name="apollo.task_manager.ParkGoRoutingTask",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="park_time",
            full_name="apollo.task_manager.ParkGoRoutingTask.park_time",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
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
        _descriptor.FieldDescriptor(
            name="routing_request",
            full_name="apollo.task_manager.ParkGoRoutingTask.routing_request",
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=423,
    serialized_end=518,
)
_TASK = _descriptor.Descriptor(
    name="Task",
    full_name="apollo.task_manager.Task",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="header",
            full_name="apollo.task_manager.Task.header",
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
            name="task_name",
            full_name="apollo.task_manager.Task.task_name",
            index=1,
            number=2,
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
            name="task_type",
            full_name="apollo.task_manager.Task.task_type",
            index=2,
            number=3,
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
        ),
        _descriptor.FieldDescriptor(
            name="cycle_routing_task",
            full_name="apollo.task_manager.Task.cycle_routing_task",
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
            name="parking_routing_task",
            full_name="apollo.task_manager.Task.parking_routing_task",
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
        _descriptor.FieldDescriptor(
            name="park_go_routing_task",
            full_name="apollo.task_manager.Task.park_go_routing_task",
            index=5,
            number=6,
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
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=521,
    serialized_end=843,
)
_CYCLEROUTINGTASK.fields_by_name[
    "routing_request"
].message_type = (
    modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2._ROUTINGREQUEST
)
_PARKINGROUTINGTASK.fields_by_name[
    "routing_request"
].message_type = (
    modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2._ROUTINGREQUEST
)
_PARKGOROUTINGTASK.fields_by_name[
    "routing_request"
].message_type = (
    modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2._ROUTINGREQUEST
)
_TASK.fields_by_name[
    "header"
].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_TASK.fields_by_name["task_type"].enum_type = _TASKTYPE
_TASK.fields_by_name["cycle_routing_task"].message_type = _CYCLEROUTINGTASK
_TASK.fields_by_name["parking_routing_task"].message_type = _PARKINGROUTINGTASK
_TASK.fields_by_name["park_go_routing_task"].message_type = _PARKGOROUTINGTASK
DESCRIPTOR.message_types_by_name["CycleRoutingTask"] = _CYCLEROUTINGTASK
DESCRIPTOR.message_types_by_name["ParkingRoutingTask"] = _PARKINGROUTINGTASK
DESCRIPTOR.message_types_by_name["ParkGoRoutingTask"] = _PARKGOROUTINGTASK
DESCRIPTOR.message_types_by_name["Task"] = _TASK
DESCRIPTOR.enum_types_by_name["TaskType"] = _TASKTYPE
DESCRIPTOR.enum_types_by_name["JunctionType"] = _JUNCTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
CycleRoutingTask = _reflection.GeneratedProtocolMessageType(
    "CycleRoutingTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _CYCLEROUTINGTASK,
        "__module__": "modules.common_msgs.task_manager_msgs.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(CycleRoutingTask)
ParkingRoutingTask = _reflection.GeneratedProtocolMessageType(
    "ParkingRoutingTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARKINGROUTINGTASK,
        "__module__": "modules.common_msgs.task_manager_msgs.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(ParkingRoutingTask)
ParkGoRoutingTask = _reflection.GeneratedProtocolMessageType(
    "ParkGoRoutingTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARKGOROUTINGTASK,
        "__module__": "modules.common_msgs.task_manager_msgs.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(ParkGoRoutingTask)
Task = _reflection.GeneratedProtocolMessageType(
    "Task",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASK,
        "__module__": "modules.common_msgs.task_manager_msgs.task_manager_pb2",
    },
)
_sym_db.RegisterMessage(Task)
