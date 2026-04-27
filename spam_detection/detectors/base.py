from abc import ABC, abstractmethod

from spam_detection.models.message import Message


class BaseDetector(ABC):
    """Abstract detector interface."""

    name: str = "base"

    @abstractmethod
    def detect(self, message: Message) -> bool:
        """Return True when a message is considered spam."""

    @abstractmethod
    def explain(self, message: Message) -> str:
        """Return a human-readable explanation."""
