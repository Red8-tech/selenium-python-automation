import csv
from pathlib import Path


class CSVReader:

    @staticmethod
    def read_data():

        project_root = Path(__file__).resolve().parents[1]
        csv_path = project_root / "data" / "test_data.csv"

        with open(
            csv_path,
            mode="r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)
