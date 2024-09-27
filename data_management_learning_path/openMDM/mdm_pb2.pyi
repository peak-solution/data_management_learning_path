from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValuesMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALCULATED: _ClassVar[ValuesMode]
    STORAGE: _ClassVar[ValuesMode]

class ScalarType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRING: _ClassVar[ScalarType]
    DATE: _ClassVar[ScalarType]
    BOOLEAN: _ClassVar[ScalarType]
    BYTE: _ClassVar[ScalarType]
    SHORT: _ClassVar[ScalarType]
    INTEGER: _ClassVar[ScalarType]
    LONG: _ClassVar[ScalarType]
    FLOAT: _ClassVar[ScalarType]
    DOUBLE: _ClassVar[ScalarType]
    BYTE_STREAM: _ClassVar[ScalarType]
    FLOAT_COMPLEX: _ClassVar[ScalarType]
    DOUBLE_COMPLEX: _ClassVar[ScalarType]
    ENUMERATION: _ClassVar[ScalarType]
    FILE_LINK: _ClassVar[ScalarType]
    BLOB: _ClassVar[ScalarType]
    UNKNOWN: _ClassVar[ScalarType]

class AxisType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    X_AXIS: _ClassVar[AxisType]
    Y_AXIS: _ClassVar[AxisType]
    XY_AXIS: _ClassVar[AxisType]

class SequenceRepresentation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPLICIT: _ClassVar[SequenceRepresentation]
    IMPLICIT_CONSTANT: _ClassVar[SequenceRepresentation]
    IMPLICIT_LINEAR: _ClassVar[SequenceRepresentation]
    IMPLICIT_SAW: _ClassVar[SequenceRepresentation]
    RAW_LINEAR: _ClassVar[SequenceRepresentation]
    RAW_POLYNOMIAL: _ClassVar[SequenceRepresentation]
    FORMULA: _ClassVar[SequenceRepresentation]
    EXPLICIT_EXTERNAL: _ClassVar[SequenceRepresentation]
    RAW_LINEAR_EXTERNAL: _ClassVar[SequenceRepresentation]
    RAW_POLYNOMIAL_EXTERNAL: _ClassVar[SequenceRepresentation]
    RAW_LINEAR_CALIBRATED: _ClassVar[SequenceRepresentation]
    RAW_LINEAR_CALIBRATED_EXTERNAL: _ClassVar[SequenceRepresentation]
CALCULATED: ValuesMode
STORAGE: ValuesMode
STRING: ScalarType
DATE: ScalarType
BOOLEAN: ScalarType
BYTE: ScalarType
SHORT: ScalarType
INTEGER: ScalarType
LONG: ScalarType
FLOAT: ScalarType
DOUBLE: ScalarType
BYTE_STREAM: ScalarType
FLOAT_COMPLEX: ScalarType
DOUBLE_COMPLEX: ScalarType
ENUMERATION: ScalarType
FILE_LINK: ScalarType
BLOB: ScalarType
UNKNOWN: ScalarType
X_AXIS: AxisType
Y_AXIS: AxisType
XY_AXIS: AxisType
EXPLICIT: SequenceRepresentation
IMPLICIT_CONSTANT: SequenceRepresentation
IMPLICIT_LINEAR: SequenceRepresentation
IMPLICIT_SAW: SequenceRepresentation
RAW_LINEAR: SequenceRepresentation
RAW_POLYNOMIAL: SequenceRepresentation
FORMULA: SequenceRepresentation
EXPLICIT_EXTERNAL: SequenceRepresentation
RAW_LINEAR_EXTERNAL: SequenceRepresentation
RAW_POLYNOMIAL_EXTERNAL: SequenceRepresentation
RAW_LINEAR_CALIBRATED: SequenceRepresentation
RAW_LINEAR_CALIBRATED_EXTERNAL: SequenceRepresentation

class ReadRequest(_message.Message):
    __slots__ = ("channel_group_id", "channel_ids", "unit_ids", "request_size", "start_index", "values_mode")
    CHANNEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    UNIT_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SIZE_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    VALUES_MODE_FIELD_NUMBER: _ClassVar[int]
    channel_group_id: str
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    unit_ids: _containers.RepeatedScalarFieldContainer[str]
    request_size: int
    start_index: int
    values_mode: ValuesMode
    def __init__(self, channel_group_id: _Optional[str] = ..., channel_ids: _Optional[_Iterable[str]] = ..., unit_ids: _Optional[_Iterable[str]] = ..., request_size: _Optional[int] = ..., start_index: _Optional[int] = ..., values_mode: _Optional[_Union[ValuesMode, str]] = ...) -> None: ...

class FloatComplex(_message.Message):
    __slots__ = ("re", "im")
    RE_FIELD_NUMBER: _ClassVar[int]
    IM_FIELD_NUMBER: _ClassVar[int]
    re: float
    im: float
    def __init__(self, re: _Optional[float] = ..., im: _Optional[float] = ...) -> None: ...

class DoubleComplex(_message.Message):
    __slots__ = ("re", "im")
    RE_FIELD_NUMBER: _ClassVar[int]
    IM_FIELD_NUMBER: _ClassVar[int]
    re: float
    im: float
    def __init__(self, re: _Optional[float] = ..., im: _Optional[float] = ...) -> None: ...

class StringArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class DateArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, values: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class BooleanArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, values: _Optional[_Iterable[bool]] = ...) -> None: ...

class ByteArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: bytes
    def __init__(self, values: _Optional[bytes] = ...) -> None: ...

class ShortArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class IntegerArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class LongArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class FloatArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class DoubleArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class ByteStreamArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, values: _Optional[_Iterable[bytes]] = ...) -> None: ...

class FloatComplexArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[FloatComplex]
    def __init__(self, values: _Optional[_Iterable[_Union[FloatComplex, _Mapping]]] = ...) -> None: ...

class DoubleComplexArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[DoubleComplex]
    def __init__(self, values: _Optional[_Iterable[_Union[DoubleComplex, _Mapping]]] = ...) -> None: ...

class MeasuredValues(_message.Message):
    __slots__ = ("name", "unit", "length", "sequence_representation", "generation_parameters", "independent", "axis_type", "scalar_type", "string_array", "date_array", "boolean_array", "byte_array", "short_array", "integer_array", "long_array", "float_array", "double_array", "byte_stream_array", "float_complex_array", "double_complex_array", "flags", "flags_full")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    INDEPENDENT_FIELD_NUMBER: _ClassVar[int]
    AXIS_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DATE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BYTE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    SHORT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    LONG_ARRAY_FIELD_NUMBER: _ClassVar[int]
    FLOAT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BYTE_STREAM_ARRAY_FIELD_NUMBER: _ClassVar[int]
    FLOAT_COMPLEX_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_COMPLEX_ARRAY_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FULL_FIELD_NUMBER: _ClassVar[int]
    name: str
    unit: str
    length: int
    sequence_representation: SequenceRepresentation
    generation_parameters: _containers.RepeatedScalarFieldContainer[float]
    independent: bool
    axis_type: AxisType
    scalar_type: ScalarType
    string_array: StringArray
    date_array: DateArray
    boolean_array: BooleanArray
    byte_array: ByteArray
    short_array: ShortArray
    integer_array: IntegerArray
    long_array: LongArray
    float_array: FloatArray
    double_array: DoubleArray
    byte_stream_array: ByteStreamArray
    float_complex_array: FloatComplexArray
    double_complex_array: DoubleComplexArray
    flags: _containers.RepeatedScalarFieldContainer[bool]
    flags_full: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., unit: _Optional[str] = ..., length: _Optional[int] = ..., sequence_representation: _Optional[_Union[SequenceRepresentation, str]] = ..., generation_parameters: _Optional[_Iterable[float]] = ..., independent: bool = ..., axis_type: _Optional[_Union[AxisType, str]] = ..., scalar_type: _Optional[_Union[ScalarType, str]] = ..., string_array: _Optional[_Union[StringArray, _Mapping]] = ..., date_array: _Optional[_Union[DateArray, _Mapping]] = ..., boolean_array: _Optional[_Union[BooleanArray, _Mapping]] = ..., byte_array: _Optional[_Union[ByteArray, _Mapping]] = ..., short_array: _Optional[_Union[ShortArray, _Mapping]] = ..., integer_array: _Optional[_Union[IntegerArray, _Mapping]] = ..., long_array: _Optional[_Union[LongArray, _Mapping]] = ..., float_array: _Optional[_Union[FloatArray, _Mapping]] = ..., double_array: _Optional[_Union[DoubleArray, _Mapping]] = ..., byte_stream_array: _Optional[_Union[ByteStreamArray, _Mapping]] = ..., float_complex_array: _Optional[_Union[FloatComplexArray, _Mapping]] = ..., double_complex_array: _Optional[_Union[DoubleComplexArray, _Mapping]] = ..., flags: _Optional[_Iterable[bool]] = ..., flags_full: _Optional[_Iterable[int]] = ...) -> None: ...

class MeasuredValuesList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[MeasuredValues]
    def __init__(self, values: _Optional[_Iterable[_Union[MeasuredValues, _Mapping]]] = ...) -> None: ...

class WriteRequestList(_message.Message):
    __slots__ = ("values",)
    class WriteRequest(_message.Message):
        __slots__ = ("channel_group_id", "channel_id", "axis_type", "independent", "explicit", "implicit_constant", "implicit_linear", "implicit_saw", "raw_linear", "raw_polynomial", "raw_linear_calibrated", "source_unit_id", "mime_type")
        class ExplicitData(_message.Message):
            __slots__ = ("string_array", "date_array", "boolean_array", "byte_array", "short_array", "integer_array", "long_array", "float_array", "double_array", "byte_stream_array", "float_complex_array", "double_complex_array", "flags", "flags_full")
            STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
            DATE_ARRAY_FIELD_NUMBER: _ClassVar[int]
            BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
            BYTE_ARRAY_FIELD_NUMBER: _ClassVar[int]
            SHORT_ARRAY_FIELD_NUMBER: _ClassVar[int]
            INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
            LONG_ARRAY_FIELD_NUMBER: _ClassVar[int]
            FLOAT_ARRAY_FIELD_NUMBER: _ClassVar[int]
            DOUBLE_ARRAY_FIELD_NUMBER: _ClassVar[int]
            BYTE_STREAM_ARRAY_FIELD_NUMBER: _ClassVar[int]
            FLOAT_COMPLEX_ARRAY_FIELD_NUMBER: _ClassVar[int]
            DOUBLE_COMPLEX_ARRAY_FIELD_NUMBER: _ClassVar[int]
            FLAGS_FIELD_NUMBER: _ClassVar[int]
            FLAGS_FULL_FIELD_NUMBER: _ClassVar[int]
            string_array: StringArray
            date_array: DateArray
            boolean_array: BooleanArray
            byte_array: ByteArray
            short_array: ShortArray
            integer_array: IntegerArray
            long_array: LongArray
            float_array: FloatArray
            double_array: DoubleArray
            byte_stream_array: ByteStreamArray
            float_complex_array: FloatComplexArray
            double_complex_array: DoubleComplexArray
            flags: _containers.RepeatedScalarFieldContainer[bool]
            flags_full: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, string_array: _Optional[_Union[StringArray, _Mapping]] = ..., date_array: _Optional[_Union[DateArray, _Mapping]] = ..., boolean_array: _Optional[_Union[BooleanArray, _Mapping]] = ..., byte_array: _Optional[_Union[ByteArray, _Mapping]] = ..., short_array: _Optional[_Union[ShortArray, _Mapping]] = ..., integer_array: _Optional[_Union[IntegerArray, _Mapping]] = ..., long_array: _Optional[_Union[LongArray, _Mapping]] = ..., float_array: _Optional[_Union[FloatArray, _Mapping]] = ..., double_array: _Optional[_Union[DoubleArray, _Mapping]] = ..., byte_stream_array: _Optional[_Union[ByteStreamArray, _Mapping]] = ..., float_complex_array: _Optional[_Union[FloatComplexArray, _Mapping]] = ..., double_complex_array: _Optional[_Union[DoubleComplexArray, _Mapping]] = ..., flags: _Optional[_Iterable[bool]] = ..., flags_full: _Optional[_Iterable[int]] = ...) -> None: ...
        class ImplicitLinear(_message.Message):
            __slots__ = ("scalar_type", "start", "increment")
            SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            INCREMENT_FIELD_NUMBER: _ClassVar[int]
            scalar_type: ScalarType
            start: float
            increment: float
            def __init__(self, scalar_type: _Optional[_Union[ScalarType, str]] = ..., start: _Optional[float] = ..., increment: _Optional[float] = ...) -> None: ...
        class ImplicitSaw(_message.Message):
            __slots__ = ("scalar_type", "start", "increment", "stop")
            SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            INCREMENT_FIELD_NUMBER: _ClassVar[int]
            STOP_FIELD_NUMBER: _ClassVar[int]
            scalar_type: ScalarType
            start: float
            increment: float
            stop: float
            def __init__(self, scalar_type: _Optional[_Union[ScalarType, str]] = ..., start: _Optional[float] = ..., increment: _Optional[float] = ..., stop: _Optional[float] = ...) -> None: ...
        class ImplicitConstant(_message.Message):
            __slots__ = ("scalar_type", "offset")
            SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            scalar_type: ScalarType
            offset: float
            def __init__(self, scalar_type: _Optional[_Union[ScalarType, str]] = ..., offset: _Optional[float] = ...) -> None: ...
        class RawLinear(_message.Message):
            __slots__ = ("scalar_type", "offset", "factor", "values")
            SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            FACTOR_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            scalar_type: ScalarType
            offset: float
            factor: float
            values: WriteRequestList.WriteRequest.ExplicitData
            def __init__(self, scalar_type: _Optional[_Union[ScalarType, str]] = ..., offset: _Optional[float] = ..., factor: _Optional[float] = ..., values: _Optional[_Union[WriteRequestList.WriteRequest.ExplicitData, _Mapping]] = ...) -> None: ...
        class RawPolynomial(_message.Message):
            __slots__ = ("scalar_type", "coefficients", "values")
            SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
            COEFFICIENTS_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            scalar_type: ScalarType
            coefficients: _containers.RepeatedScalarFieldContainer[float]
            values: WriteRequestList.WriteRequest.ExplicitData
            def __init__(self, scalar_type: _Optional[_Union[ScalarType, str]] = ..., coefficients: _Optional[_Iterable[float]] = ..., values: _Optional[_Union[WriteRequestList.WriteRequest.ExplicitData, _Mapping]] = ...) -> None: ...
        class RawLinearCalibrated(_message.Message):
            __slots__ = ("scalar_type", "offset", "factor", "calibration", "values")
            SCALAR_TYPE_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            FACTOR_FIELD_NUMBER: _ClassVar[int]
            CALIBRATION_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            scalar_type: ScalarType
            offset: float
            factor: float
            calibration: float
            values: WriteRequestList.WriteRequest.ExplicitData
            def __init__(self, scalar_type: _Optional[_Union[ScalarType, str]] = ..., offset: _Optional[float] = ..., factor: _Optional[float] = ..., calibration: _Optional[float] = ..., values: _Optional[_Union[WriteRequestList.WriteRequest.ExplicitData, _Mapping]] = ...) -> None: ...
        CHANNEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        AXIS_TYPE_FIELD_NUMBER: _ClassVar[int]
        INDEPENDENT_FIELD_NUMBER: _ClassVar[int]
        EXPLICIT_FIELD_NUMBER: _ClassVar[int]
        IMPLICIT_CONSTANT_FIELD_NUMBER: _ClassVar[int]
        IMPLICIT_LINEAR_FIELD_NUMBER: _ClassVar[int]
        IMPLICIT_SAW_FIELD_NUMBER: _ClassVar[int]
        RAW_LINEAR_FIELD_NUMBER: _ClassVar[int]
        RAW_POLYNOMIAL_FIELD_NUMBER: _ClassVar[int]
        RAW_LINEAR_CALIBRATED_FIELD_NUMBER: _ClassVar[int]
        SOURCE_UNIT_ID_FIELD_NUMBER: _ClassVar[int]
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        channel_group_id: str
        channel_id: str
        axis_type: AxisType
        independent: bool
        explicit: WriteRequestList.WriteRequest.ExplicitData
        implicit_constant: WriteRequestList.WriteRequest.ImplicitConstant
        implicit_linear: WriteRequestList.WriteRequest.ImplicitLinear
        implicit_saw: WriteRequestList.WriteRequest.ImplicitSaw
        raw_linear: WriteRequestList.WriteRequest.RawLinear
        raw_polynomial: WriteRequestList.WriteRequest.RawPolynomial
        raw_linear_calibrated: WriteRequestList.WriteRequest.RawLinearCalibrated
        source_unit_id: str
        mime_type: str
        def __init__(self, channel_group_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., axis_type: _Optional[_Union[AxisType, str]] = ..., independent: bool = ..., explicit: _Optional[_Union[WriteRequestList.WriteRequest.ExplicitData, _Mapping]] = ..., implicit_constant: _Optional[_Union[WriteRequestList.WriteRequest.ImplicitConstant, _Mapping]] = ..., implicit_linear: _Optional[_Union[WriteRequestList.WriteRequest.ImplicitLinear, _Mapping]] = ..., implicit_saw: _Optional[_Union[WriteRequestList.WriteRequest.ImplicitSaw, _Mapping]] = ..., raw_linear: _Optional[_Union[WriteRequestList.WriteRequest.RawLinear, _Mapping]] = ..., raw_polynomial: _Optional[_Union[WriteRequestList.WriteRequest.RawPolynomial, _Mapping]] = ..., raw_linear_calibrated: _Optional[_Union[WriteRequestList.WriteRequest.RawLinearCalibrated, _Mapping]] = ..., source_unit_id: _Optional[str] = ..., mime_type: _Optional[str] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[WriteRequestList.WriteRequest]
    def __init__(self, values: _Optional[_Iterable[_Union[WriteRequestList.WriteRequest, _Mapping]]] = ...) -> None: ...

class PreviewRequest(_message.Message):
    __slots__ = ("read_request", "number_of_chunks")
    READ_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    read_request: ReadRequest
    number_of_chunks: int
    def __init__(self, read_request: _Optional[_Union[ReadRequest, _Mapping]] = ..., number_of_chunks: _Optional[int] = ...) -> None: ...

class PreviewValuesList(_message.Message):
    __slots__ = ("min", "avg", "max")
    MIN_FIELD_NUMBER: _ClassVar[int]
    AVG_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: _containers.RepeatedCompositeFieldContainer[MeasuredValues]
    avg: _containers.RepeatedCompositeFieldContainer[MeasuredValues]
    max: _containers.RepeatedCompositeFieldContainer[MeasuredValues]
    def __init__(self, min: _Optional[_Iterable[_Union[MeasuredValues, _Mapping]]] = ..., avg: _Optional[_Iterable[_Union[MeasuredValues, _Mapping]]] = ..., max: _Optional[_Iterable[_Union[MeasuredValues, _Mapping]]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("source", "type", "id", "label", "serial", "leaf", "idAttribute", "filter", "level")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    LEAF_FIELD_NUMBER: _ClassVar[int]
    IDATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    source: str
    type: str
    id: str
    label: str
    serial: str
    leaf: bool
    idAttribute: str
    filter: str
    level: int
    def __init__(self, source: _Optional[str] = ..., type: _Optional[str] = ..., id: _Optional[str] = ..., label: _Optional[str] = ..., serial: _Optional[str] = ..., leaf: bool = ..., idAttribute: _Optional[str] = ..., filter: _Optional[str] = ..., level: _Optional[int] = ...) -> None: ...

class NodeProviderResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, data: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("channel_group_id", "channel_id", "axis_type", "independent", "global_flag", "flags", "mime_type", "flags_full")
    CHANNEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    AXIS_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEPENDENT_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_FLAG_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FULL_FIELD_NUMBER: _ClassVar[int]
    channel_group_id: str
    channel_id: str
    axis_type: AxisType
    independent: bool
    global_flag: bool
    flags: _containers.RepeatedScalarFieldContainer[bool]
    mime_type: str
    flags_full: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, channel_group_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., axis_type: _Optional[_Union[AxisType, str]] = ..., independent: bool = ..., global_flag: bool = ..., flags: _Optional[_Iterable[bool]] = ..., mime_type: _Optional[str] = ..., flags_full: _Optional[_Iterable[int]] = ...) -> None: ...
