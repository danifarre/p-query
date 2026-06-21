import textwrap
from datasource.csv_data_source import CSVDataSource
from datatypes.schema import Schema, Field
from datatypes.data_types import DataTypes

def test_csv_datasource_integration_end_to_end(tmp_path):
    csv_file = tmp_path / "integration.csv"

    csv_content = textwrap.dedent("""
            id,name
            1,Alice
            2,Bob
            3,Charlie
            4,David
            5,Eve
            6,Frank
            7,Grace
        """).strip()

    csv_file.write_text(csv_content, encoding="utf-8")

    real_schema = Schema([
        Field("id", DataTypes.Int32Type),
        Field("name", DataTypes.StringType),
    ])

    datasource = CSVDataSource(filename=str(csv_file), schema=real_schema)

    datasource._batch_size = 5

    iterator = datasource.scan(projection=[])
    batches = list(iterator)

    assert len(batches) == 2, "The generator did not split the batches correctly"

    batch_1 = batches[0]

    assert len(batch_1.fields[0]) == 5

    assert batch_1.fields[0].to_list() == [1, 2, 3, 4, 5]
    assert batch_1.fields[1].to_list() == ["Alice", "Bob", "Charlie", "David", "Eve"]

    batch_2 = batches[1]

    assert len(batch_2.fields[0]) == 2
    assert batch_2.fields[0].to_list() == [6, 7]
    assert batch_2.fields[1].to_list() == ["Frank", "Grace"]