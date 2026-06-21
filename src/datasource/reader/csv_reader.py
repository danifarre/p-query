import csv
from typing import Dict, Any

class CsvReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file = None
        self.csv_reader = None

    def __enter__(self):
        self.file = open(self.file_path, mode='r', encoding='utf-8')
        self.csv_reader = csv.DictReader(self.file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def next_record(self) -> Dict[str, Any]:
        return next(self.csv_reader)