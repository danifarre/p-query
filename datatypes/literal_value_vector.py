from dataclasses import dataclass
from typing import Any

import pyarrow as pa

from datatypes.column_vector import ColumnVector

@dataclass
class LiteralValueVector(ColumnVector):
    arrow_type: pa.DataType
    value: Any
    size: int

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, i: int) -> Any:
        if i < 0 or i >= self.size:
            raise IndexError
        return self.value

    @property
    def data_type(self) -> pa.DataType:
        return self.arrow_type
