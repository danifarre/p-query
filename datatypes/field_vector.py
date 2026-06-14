from dataclasses import dataclass
from typing import Any

import pyarrow as pa

from datatypes.column_vector import ColumnVector
from datatypes.data_types import DataTypes

@dataclass
class FieldVector(ColumnVector):
    field: pa.Array

    def __len__(self) -> int:
        return len(self.field)

    def __getitem__(self, i: int) -> Any:
        if self.field is None:
            return None

        return self.field[i]

    @property
    def data_type(self) -> pa.DataType:
        match self.field:
            case pa.BooleanArray:
                return DataTypes.BooleanType
            case pa.Int8Array:
                return DataTypes.Int8Type
            case pa.Int16Arra:
                return DataTypes.Int16Type
            case pa.Int32Arra:
                return DataTypes.Int32Type
            case pa.Int64Array:
                return DataTypes.Int64Type
            case pa.FloatArray:
                return DataTypes.FloatType
            case pa.DoubleArray:
                return DataTypes.DoubleType
            case pa.StringArray:
                return DataTypes.StringType
            case _:
                raise TypeError(f"Unsupported pyarrow array type: {type(self.field).__name__}")
