from datasource.csv_data_source import CSVDataSource
from datatypes.data_types import DataTypes
from datatypes.schema import Schema, Field


def test_reader_as_iterator_creates_correct_batches(mocker):
    mock_csv_reader = mocker.patch("datasource.csv_data_source.CsvReader")
    schema = Schema([
        Field("id", DataTypes.Int32Type),
        Field("nombre", DataTypes.StringType),
    ])

    mock_reader_instance = mock_csv_reader.return_value

    def mock_data():
        for i in range(1, 8):
            yield {"id": i, "nombre": f"Letra {i}"}
        while True:
            yield None

    mock_reader_instance.next_record.side_effect = mock_data()

    datasource = CSVDataSource("dummy.csv", schema=schema)
    datasource._batch_size = 5

    iterator = datasource.scan(projection=[])
    batches = list(iterator)

    assert len(batches) == 2
    assert len(batches[0].fields[0]) == 5
    assert len(batches[1].fields[0]) == 2
