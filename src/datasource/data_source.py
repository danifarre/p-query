from abc import ABC, abstractmethod
from typing import List

from datatypes.record_batch import RecordBatch
from datatypes.schema import Schema


class DataSource(ABC):

    @abstractmethod
    def schema(self) -> Schema:
        """
        Return the schema for the underlying data source
        """

        ...

    @abstractmethod
    def scan(self, projection: List[str]) -> RecordBatch:
        """
        Scan the data source, selecting the specified columns
        """

        ...
