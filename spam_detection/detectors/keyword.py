from spam_detection.detectors.base import BaseDetector
from spam_detection.models.message import Message


class KeywordDetector(BaseDetector):
    """Detect spam using suspicious marketing keywords."""

    name = "keyword"

    def __init__(self, keywords: list[str] | None = None) -> None:
        self._keywords = keywords or [
            "win",
            "winner",
            "free",
            "prize",
            "claim",
            "urgent",
            "offer",
            "bonus",
            "money",
            "click",
        ]

    def detect(self, message: Message) -> bool:
        text = message.text.lower()
        return any(keyword in text for keyword in self._keywords)

    def explain(self, message: Message) -> str:
        text = message.text.lower()
        matched = [keyword for keyword in self._keywords if keyword in text]
        if not matched:
            return "No suspicious keywords were found."
        return f"Matched suspicious keywords: {', '.join(matched)}."
