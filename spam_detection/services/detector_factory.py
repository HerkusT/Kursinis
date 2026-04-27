from spam_detection.detectors.base import BaseDetector
from spam_detection.detectors.blacklist import BlacklistDetector
from spam_detection.detectors.frequency import FrequencyDetector
from spam_detection.detectors.keyword import KeywordDetector


class DetectorFactory:
    """Factory Method pattern for detector creation."""

    @staticmethod
    def create_detector(detector_type: str) -> BaseDetector:
        detector_type = detector_type.lower()

        if detector_type == "keyword":
            return KeywordDetector()
        if detector_type == "blacklist":
            return BlacklistDetector()
        if detector_type == "frequency":
            return FrequencyDetector()

        raise ValueError(f"Unknown detector type: {detector_type}")
