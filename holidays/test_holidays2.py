import unittest
from unittest.mock import Mock
import holidays


class TestCalendar(unittest.TestCase):
    def test_get_holidays_success(self):
        # Mock the requests.get method to return a successful response
        requests = Mock()
        requests.get.return_value.status_code = 200
        requests.get.return_value.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }

        # Temporarily replace the requests.get method with the mocked version
        original_requests_get = holidays.requests.get
        holidays.requests.get = requests.get

        # Test that the get_holidays function returns the expected result
        result = holidays.get_holidays()
        self.assertEqual(result["12/25"], "Christmas")
        self.assertEqual(result["7/4"], "Independence Day")

        # Restore the original requests.get method
        holidays.requests.get = original_requests_get

    def test_get_holidays_failure(self):
        # Mock the requests.get method to return a failed response
        requests = Mock()
        requests.get.return_value.status_code = 404

        # Temporarily replace the requests.get method with the mocked version
        original_requests_get = holidays.requests.get
        holidays.requests.get = requests.get

        # Test that the get_holidays function returns None when the response is not successful
        result = holidays.get_holidays()
        self.assertIsNone(result)

        # Restore the original requests.get method
        holidays.requests.get = original_requests_get
