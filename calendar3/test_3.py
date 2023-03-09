import requests
import unittest
from unittest.mock import Mock
from calendar3 import get_holidays


class TestCalendar(unittest.TestCase):
    def test_success3(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
            "1/1": "New Year's Day",
        }

        requests.get.side_effect = [mock_response]

        # Test that the get_holidays function returns the expected result
        result = get_holidays()
        self.assertEqual(result["12/25"], "Christmas")
        self.assertEqual(result["7/4"], "Independence Day")

    def test_success3b(self):
        # Mock the requests.get method to return a successful response
        # requests = Mock()
        requests.get.side_effect = lambda url: Mock(
            status_code=200,
            json=lambda: {
                "12/25": "Christmas",
                "7/4": "Independence Day",
            },
        )

        # Test that the get_holidays function returns the expected result
        result = get_holidays()
        self.assertEqual(result["12/25"], "Christmas")
        self.assertEqual(result["7/4"], "Independence Day")


    def test_failure3(self):
        # Mock the requests.get method to return a failed response
        requests.get.side_effect = lambda url: Mock(status_code=404)

        # Test that the get_holidays function returns None when the response is not successful
        self.assertIsNone(get_holidays())
