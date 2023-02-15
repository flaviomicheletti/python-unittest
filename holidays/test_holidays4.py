import unittest
import requests
from unittest.mock import Mock
from holidays import get_holidays


class TestCalendar(unittest.TestCase):
    def test_success4(self):
        # Save the original requests.get function
        original_get = requests.get

        # Define a new function to replace requests.get that returns a successful response
        def mock(url):
            return Mock(
                status_code=200,
                json=lambda: {
                    "12/25": "Christmas",
                    "7/4": "Independence Day",
                    "1/1": "New Year's Day",
                },
            )

        # Replace requests.get with the mock function
        requests.get = mock

        # Test that the get_holidays function returns the expected actual
        actual = get_holidays()
        self.assertEqual(actual["12/25"], "Christmas")
        self.assertEqual(actual["7/4"], "Independence Day")

        # Restore the original requests.get function
        requests.get = original_get
