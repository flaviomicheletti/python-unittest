# test_my_module.py
import unittest
from unittest.mock import MagicMock, patch
from my_module1 import send_email


class TestSendEmail(unittest.TestCase):
    def test_send_email(self):
        with patch("smtplib.SMTP") as mock_smtp:
            smtp_instance = mock_smtp.return_value
            smtp_instance.starttls.return_value = None
            smtp_instance.login.return_value = None
            smtp_instance.sendmail.return_value = None
            smtp_instance.quit.return_value = None

            send_email(
                "from@example.com", "to@example.com", "Test Subject", "Test Body"
            )

            smtp_instance.starttls.assert_called_once()
            smtp_instance.login.assert_called_once_with("user@gmail.com", "password")
            smtp_instance.sendmail.assert_called_once_with(
                "from@example.com",
                "to@example.com",
                f"From: from@example.com\nTo: to@example.com\nSubject: Test Subject\n\nTest Body",
            )
            smtp_instance.quit.assert_called_once()
