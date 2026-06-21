from typing import cast, Iterator, List, Any, Dict

import pyarrow as pa
import pyarrow.compute as pc

from datasource.data_source import DataSource
from datasource.reader.csv_reader import CsvReader
from datatypes.field_vector import FieldVector
from datatypes.record_batch import RecordBatch
from datatypes.schema import Schema


class CSVDataSource(DataSource):

    def __init__(self, filename: str, schema: Schema | None = None):
        self.filename = filename
        self.schema = schema

        self._has_headers = True
        self._batch_size = 5

        self._cached_final_schema: Schema | None = None

    def scan(self, projection: List[str]) -> Iterator[RecordBatch]:
        if len(projection) != 0:
            read_schema = self._final_schema.select(projection)
        else:
            read_schema = self._final_schema

        return self._reader_as_iterator(read_schema)

    def schema(self) -> Schema:
        ...

    @property
    def _final_schema(self) -> Schema:
        if self._cached_final_schema is None:
            self._cached_final_schema = self.schema if self.schema is not None else self.infer_schema()

        return cast(Schema, self._cached_final_schema)

    def infer_schema(self) -> Schema:
        ...

    def _reader_as_iterator(self, schema: Schema) -> Iterator[RecordBatch]:
        with CsvReader(self.filename) as reader:
            batch = []
            try:
                while True:
                    line = reader.next_record()
                    batch.append(line)

                    if len(batch) == self._batch_size:
                        yield self._create_batch(batch, schema)
                        batch = []

            except StopIteration:
                if batch:
                    yield self._create_batch(batch, schema)

    @staticmethod
    def _create_batch(rows: List[Dict[str, Any]], schema: Schema) -> RecordBatch:
        field_vectors = []
        for field in schema.fields:
            raw_array = pa.array([row[field.name] for row in rows])

            casted_array = pc.cast(raw_array, field.data_type)

            field_vector = FieldVector(casted_array)
            field_vectors.append(field_vector)

        return RecordBatch(schema, field_vectors)
