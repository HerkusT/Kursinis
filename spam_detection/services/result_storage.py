import csv
from pathlib import Path
from typing import Iterable


class ResultStorage:
    """Handles exporting detection results to CSV files."""

    def save_results(self, file_path: str, rows: Iterable[dict[str, str]]) -> None:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = list(rows)
        if not rows:
            return

        with path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
