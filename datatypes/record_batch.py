from dataclasses import dataclass
from typing import List

from datatypes.column_vector import ColumnVector
from datatypes.schema import Schema


@dataclass
class RecordBatch:
    schema: Schema
    fields: List[ColumnVector]

    def row_count(self) -> int:
        return len(self.fields[0])

    def column_count(self) -> int:
        return len(self.fields)

    def __getitem__(self, i: int) -> ColumnVector:
        return self.fields[i]
