import unittest
from enum import Enum
from unittest.mock import patch

from lesson_013.homework_10 import log_event

USERNAME = "Matvey"


class Status(Enum):
    SUCCESS = "success"
    EXPIRED = "expired"
    FAILED = "failed"
    UNKNOWN = "unknown"


class TestLogEvent(unittest.TestCase):

    @patch("logging.getLogger")
    def test_status_logging(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value

        test_cases = [
            (Status.SUCCESS, "info"),
            (Status.EXPIRED, "warning"),
            (Status.FAILED, "error"),
            (Status.UNKNOWN, "error"),
        ]

        for status, method_name in test_cases:
            with self.subTest(status=status):
                mock_logger.reset_mock()
                log_event(USERNAME, status.value)
                expected_message = (
                    f"Login event - Username: {USERNAME}, Status: {status.value}"
                )
                getattr(mock_logger, method_name).assert_called_once_with(expected_message)


if __name__ == "__main__":
    unittest.main()
