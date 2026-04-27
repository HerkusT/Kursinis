import tempfile
import unittest
from pathlib import Path

from spam_detection.detectors.blacklist import BlacklistDetector
from spam_detection.detectors.frequency import FrequencyDetector
from spam_detection.detectors.keyword import KeywordDetector
from spam_detection.models.message import Message
from spam_detection.services.detector_factory import DetectorFactory
from spam_detection.services.result_storage import ResultStorage
from spam_detection.services.spam_system import SpamDetectionSystem
from spam_detection.utils.file_manager import FileManager


class TestSpamDetectionSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.keyword_detector = KeywordDetector()
        self.blacklist_detector = BlacklistDetector({"bad_sender"})
        self.frequency_detector = FrequencyDetector()
        self.system = SpamDetectionSystem(
            [
                self.keyword_detector,
                self.blacklist_detector,
                self.frequency_detector,
            ]
        )

    def test_keyword_detector_identifies_spam(self) -> None:
        message = Message(sender="alice", _text="Win free money now")
        self.assertTrue(self.keyword_detector.detect(message))

    def test_blacklist_detector_identifies_spam(self) -> None:
        message = Message(sender="bad_sender", _text="Hello")
        self.assertTrue(self.blacklist_detector.detect(message))

    def test_frequency_detector_identifies_spam(self) -> None:
        message = Message(sender="promo", _text="BUY NOW!!!! VISIT HTTP://SPAM.COM")
        self.assertTrue(self.frequency_detector.detect(message))

    def test_system_returns_not_spam_for_normal_message(self) -> None:
        message = Message(sender="friend", _text="Hi, are we meeting at 5?")
        result = self.system.analyze_message(message)
        self.assertFalse(result["is_spam"])
        self.assertEqual(result["label"], "NOT SPAM")

    def test_factory_creates_keyword_detector(self) -> None:
        detector = DetectorFactory.create_detector("keyword")
        self.assertIsInstance(detector, KeywordDetector)

    def test_file_manager_loads_messages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "messages.csv"
            file_path.write_text("sender,text\nalice,Hello\nbob,Free prize\n", encoding="utf-8")
            manager = FileManager()
            messages = manager.load_messages(str(file_path))
            self.assertEqual(len(messages), 2)
            self.assertEqual(messages[1].sender, "bob")

    def test_result_storage_saves_csv(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "results.csv"
            storage = ResultStorage()
            storage.save_results(
                str(file_path),
                [
                    {
                        "sender": "alice",
                        "text": "hello",
                        "is_spam": False,
                        "label": "NOT SPAM",
                        "detected_by": "none",
                        "explanation": "No suspicious keywords were found.",
                    }
                ],
            )
            self.assertTrue(file_path.exists())
            saved_text = file_path.read_text(encoding="utf-8")
            self.assertIn("NOT SPAM", saved_text)


if __name__ == "__main__":
    unittest.main()
