"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(
    name="modules/planning/proto/math/qp_problem.proto",
    package="apollo.planning",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n,modules/planning/proto/math/qp_problem.proto\x12\x0fapollo.planning"\xbd\x02\n\x1bQuadraticProgrammingProblem\x12\x12\n\nparam_size\x18\x01 \x01(\x05\x123\n\x10quadratic_matrix\x18\x02 \x01(\x0b2\x19.apollo.planning.QPMatrix\x12\x0c\n\x04bias\x18\x03 \x03(\x01\x122\n\x0fequality_matrix\x18\x04 \x01(\x0b2\x19.apollo.planning.QPMatrix\x12\x16\n\x0eequality_value\x18\x05 \x03(\x01\x124\n\x11inequality_matrix\x18\x06 \x01(\x0b2\x19.apollo.planning.QPMatrix\x12\x18\n\x10inequality_value\x18\x07 \x03(\x01\x12\x14\n\x0cinput_marker\x18\x08 \x03(\x01\x12\x15\n\roptimal_param\x18\t \x03(\x01"?\n\x08QPMatrix\x12\x10\n\x08row_size\x18\x01 \x01(\x05\x12\x10\n\x08col_size\x18\x02 \x01(\x05\x12\x0f\n\x07element\x18\x03 \x03(\x01"_\n\x1eQuadraticProgrammingProblemSet\x12=\n\x07problem\x18\x01 \x03(\x0b2,.apollo.planning.QuadraticProgrammingProblem',
)
_QUADRATICPROGRAMMINGPROBLEM = _descriptor.Descriptor(
    name="QuadraticProgrammingProblem",
    full_name="apollo.planning.QuadraticProgrammingProblem",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="param_size",
            full_name="apollo.planning.QuadraticProgrammingProblem.param_size",
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
            name="quadratic_matrix",
            full_name="apollo.planning.QuadraticProgrammingProblem.quadratic_matrix",
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
            name="bias",
            full_name="apollo.planning.QuadraticProgrammingProblem.bias",
            index=2,
            number=3,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="equality_matrix",
            full_name="apollo.planning.QuadraticProgrammingProblem.equality_matrix",
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
            name="equality_value",
            full_name="apollo.planning.QuadraticProgrammingProblem.equality_value",
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="inequality_matrix",
            full_name="apollo.planning.QuadraticProgrammingProblem.inequality_matrix",
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
        _descriptor.FieldDescriptor(
            name="inequality_value",
            full_name="apollo.planning.QuadraticProgrammingProblem.inequality_value",
            index=6,
            number=7,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="input_marker",
            full_name="apollo.planning.QuadraticProgrammingProblem.input_marker",
            index=7,
            number=8,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="optimal_param",
            full_name="apollo.planning.QuadraticProgrammingProblem.optimal_param",
            index=8,
            number=9,
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
    serialized_start=66,
    serialized_end=383,
)
_QPMATRIX = _descriptor.Descriptor(
    name="QPMatrix",
    full_name="apollo.planning.QPMatrix",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="row_size",
            full_name="apollo.planning.QPMatrix.row_size",
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
            name="col_size",
            full_name="apollo.planning.QPMatrix.col_size",
            index=1,
            number=2,
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
            name="element",
            full_name="apollo.planning.QPMatrix.element",
            index=2,
            number=3,
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
    serialized_start=385,
    serialized_end=448,
)
_QUADRATICPROGRAMMINGPROBLEMSET = _descriptor.Descriptor(
    name="QuadraticProgrammingProblemSet",
    full_name="apollo.planning.QuadraticProgrammingProblemSet",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="problem",
            full_name="apollo.planning.QuadraticProgrammingProblemSet.problem",
            index=0,
            number=1,
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
    serialized_start=450,
    serialized_end=545,
)
_QUADRATICPROGRAMMINGPROBLEM.fields_by_name["quadratic_matrix"].message_type = _QPMATRIX
_QUADRATICPROGRAMMINGPROBLEM.fields_by_name["equality_matrix"].message_type = _QPMATRIX
_QUADRATICPROGRAMMINGPROBLEM.fields_by_name[
    "inequality_matrix"
].message_type = _QPMATRIX
_QUADRATICPROGRAMMINGPROBLEMSET.fields_by_name[
    "problem"
].message_type = _QUADRATICPROGRAMMINGPROBLEM
DESCRIPTOR.message_types_by_name[
    "QuadraticProgrammingProblem"
] = _QUADRATICPROGRAMMINGPROBLEM
DESCRIPTOR.message_types_by_name["QPMatrix"] = _QPMATRIX
DESCRIPTOR.message_types_by_name[
    "QuadraticProgrammingProblemSet"
] = _QUADRATICPROGRAMMINGPROBLEMSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
QuadraticProgrammingProblem = _reflection.GeneratedProtocolMessageType(
    "QuadraticProgrammingProblem",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUADRATICPROGRAMMINGPROBLEM,
        "__module__": "modules.planning.proto.math.qp_problem_pb2",
    },
)
_sym_db.RegisterMessage(QuadraticProgrammingProblem)
QPMatrix = _reflection.GeneratedProtocolMessageType(
    "QPMatrix",
    (_message.Message,),
    {
        "DESCRIPTOR": _QPMATRIX,
        "__module__": "modules.planning.proto.math.qp_problem_pb2",
    },
)
_sym_db.RegisterMessage(QPMatrix)
QuadraticProgrammingProblemSet = _reflection.GeneratedProtocolMessageType(
    "QuadraticProgrammingProblemSet",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUADRATICPROGRAMMINGPROBLEMSET,
        "__module__": "modules.planning.proto.math.qp_problem_pb2",
    },
)
_sym_db.RegisterMessage(QuadraticProgrammingProblemSet)
