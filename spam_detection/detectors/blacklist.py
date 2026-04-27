from spam_detection.detectors.base import BaseDetector
from spam_detection.models.message import Message


class BlacklistDetector(BaseDetector):
    """Detect spam using a list of blocked senders."""

    name = "blacklist"

    def __init__(self, blocked_senders: set[str] | None = None) -> None:
        self._blocked_senders = blocked_senders or {
            "unknown_offer",
            "lottery_agent",
            "crypto_fastcash",
        }

    def detect(self, message: Message) -> bool:
        return message.sender.lower() in self._blocked_senders

    def explain(self, message: Message) -> str:
        if self.detect(message):
            return f"Sender '{message.sender}' exists in the blocked senders list."
        return "Sender is not blacklisted."
