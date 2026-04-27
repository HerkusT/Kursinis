from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Message:
    """Represents a single text message for analysis."""

    sender: str
    _text: str = field(repr=False)

    @property
    def text(self) -> str:
        """Read-only access to message text."""
        return self._text

    def to_dict(self) -> Dict[str, str]:
        return {"sender": self.sender, "text": self.text}
