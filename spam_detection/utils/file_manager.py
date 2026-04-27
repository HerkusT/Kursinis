import csv
from pathlib import Path

from spam_detection.models.message import Message


class FileManager:
    """Reads message data from CSV files."""

    REQUIRED_FIELDS = {"sender", "text"}

    def load_messages(self, file_path: str) -> list[Message]:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open("r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            if reader.fieldnames is None:
                raise ValueError("CSV file must include a header row.")

            missing = self.REQUIRED_FIELDS.difference(reader.fieldnames)
            if missing:
                missing_fields = ", ".join(sorted(missing))
                raise ValueError(f"CSV file is missing required fields: {missing_fields}")

            messages = [
                Message(sender=row["sender"].strip(), _text=row["text"].strip())
                for row in reader
                if row.get("sender") and row.get("text")
            ]

        return messages
