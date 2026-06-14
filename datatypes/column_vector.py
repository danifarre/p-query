from abc import ABC, abstractmethod
from typing import Any
import pyarrow as pa

class ColumnVector(ABC):

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, i: int) -> Any:
        pass

    @property
    @abstractmethod
    def data_type(self) -> pa.DataType:
        pass
