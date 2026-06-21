from dataclasses import dataclass
from typing import List

import pyarrow as pa


@dataclass
class Field:
    name: str
    data_type: pa.DataType

    def to_arrow(self) -> pa.Field:
        return pa.field(self.name, self.data_type)


@dataclass
class Schema:
    fields: List[Field]

    def select(self, fields: List[str]) -> 'Schema':
        return Schema([field for field in self.fields if field.name in fields])

    def to_arrow(self) -> pa.Schema:
        return pa.Schema([arrow_field.to_arrow() for arrow_field in self.fields])
