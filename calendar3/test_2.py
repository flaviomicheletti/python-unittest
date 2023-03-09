import unittest
from unittest.mock import Mock
import calendar3


class TestCalendar(unittest.TestCase):
    def test_success2(self):
        # Mock the requests.get method to return a successful response
        requests_mock = Mock()
        requests_mock.get.return_value.status_code = 200
        requests_mock.get.return_value.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }

        # Temporarily replace the requests.get method with the mocked version
        original_requests_get = calendar3.requests.get
        calendar3.requests.get = requests_mock.get

        # Test that the get_holidays function returns the expected result
        result = calendar3.get_holidays()
        self.assertEqual(result["12/25"], "Christmas")
        self.assertEqual(result["7/4"], "Independence Day")

        # Restore the original requests.get method
        calendar3.requests.get = original_requests_get

    def test_failure2(self):
        # Mock the requests.get method to return a failed response
        requests = Mock()
        requests.get.return_value.status_code = 404

        # Temporarily replace the requests.get method with the mocked version
        original_requests_get = calendar3.requests.get
        calendar3.requests.get = requests.get

        # Test that the get_holidays function returns None when the response is not successful
        result = calendar3.get_holidays()
        self.assertIsNone(result)

        # Restore the original requests.get method
        calendar3.requests.get = original_requests_get
