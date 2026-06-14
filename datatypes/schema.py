from dataclasses import dataclass
from typing import List

import pyarrow as pa


@dataclass
class Field:
    name: str
    data_type: pa.DataType

    def to_arrow(self) -> pa.Field:
        return pa.Field(self.name, self.data_type)


@dataclass
class Schema:
    fields: List[Field]

    def to_arrow(self) -> pa.Schema:
        return pa.Schema([arrow_field.to_arrow() for arrow_field in self.fields])
