from abc import ABC, abstractmethod
from typing import Any

import pyarrow as pa


class ColumnVector(ABC):

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __getitem__(self, i: int) -> Any:
        ...

    @abstractmethod
    def to_list(self):
        ...

    @property
    @abstractmethod
    def data_type(self) -> pa.DataType:
        ...
