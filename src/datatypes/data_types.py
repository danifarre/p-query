import pyarrow as pa


class DataTypes:
    BooleanType: pa.DataType = pa.bool_()

    Int8Type: pa.DataType = pa.int8()
    Int16Type: pa.DataType = pa.int16()
    Int32Type: pa.DataType = pa.int32()
    Int64Type: pa.DataType = pa.int64()

    UInt8Type: pa.DataType = pa.uint8()
    UInt16Type: pa.DataType = pa.uint16()
    UInt32Type: pa.DataType = pa.uint32()
    UInt64Type: pa.DataType = pa.uint64()

    FloatType: pa.DataType = pa.float32()
    DoubleType: pa.DataType = pa.float64()

    StringType: pa.DataType = pa.string()
