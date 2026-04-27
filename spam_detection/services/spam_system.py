from spam_detection.detectors.base import BaseDetector
from spam_detection.models.message import Message


class SpamDetectionSystem:
    """Main application service using composition of multiple detectors."""

    def __init__(self, detectors: list[BaseDetector]) -> None:
        self._detectors = detectors

    @property
    def detectors(self) -> tuple[BaseDetector, ...]:
        return tuple(self._detectors)

    def analyze_message(self, message: Message) -> dict[str, str | bool]:
        results = []
        explanations = []

        for detector in self._detectors:
            is_spam = detector.detect(message)
            results.append(is_spam)
            explanations.append(f"{detector.name}: {detector.explain(message)}")

        detected_by = [detector.name for detector in self._detectors if detector.detect(message)]
        is_spam = any(results)

        return {
            "sender": message.sender,
            "text": message.text,
            "is_spam": is_spam,
            "label": "SPAM" if is_spam else "NOT SPAM",
            "detected_by": ", ".join(detected_by) if detected_by else "none",
            "explanation": " | ".join(explanations),
        }
