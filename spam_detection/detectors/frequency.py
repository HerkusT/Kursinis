from spam_detection.detectors.base import BaseDetector
from spam_detection.models.message import Message


class FrequencyDetector(BaseDetector):
    """Detect spam using simple text frequency heuristics."""

    name = "frequency"

    def __init__(self, max_uppercase_ratio: float = 0.45, max_links: int = 1) -> None:
        self._max_uppercase_ratio = max_uppercase_ratio
        self._max_links = max_links

    def detect(self, message: Message) -> bool:
        text = message.text
        if not text:
            return False

        letters = [char for char in text if char.isalpha()]
        uppercase_ratio = (
            sum(char.isupper() for char in letters) / len(letters) if letters else 0.0
        )
        links_count = text.lower().count("http") + text.lower().count("www")
        exclamation_count = text.count("!")

        return (
            uppercase_ratio > self._max_uppercase_ratio
            or links_count > self._max_links
            or exclamation_count >= 4
        )

    def explain(self, message: Message) -> str:
        text = message.text
        letters = [char for char in text if char.isalpha()]
        uppercase_ratio = (
            sum(char.isupper() for char in letters) / len(letters) if letters else 0.0
        )
        links_count = text.lower().count("http") + text.lower().count("www")
        exclamation_count = text.count("!")
        return (
            "Heuristic values -> "
            f"uppercase_ratio={uppercase_ratio:.2f}, "
            f"links={links_count}, exclamations={exclamation_count}."
        )
