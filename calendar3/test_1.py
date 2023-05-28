import unittest
from unittest.mock import Mock
import calendar3


class TestCalendar(unittest.TestCase):
    def test_success1(self):
        # Mock the requests.get method to return a successful response
        requests_mock = Mock()
        requests_mock.get.return_value.status_code = 200
        requests_mock.get.return_value.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }

        # Test that the get_holidays function returns the expected result
        with unittest.mock.patch("calendar3.requests", requests_mock):
            result = calendar3.get_holidays()
            
        self.assertEqual(result["12/25"], "Christmas")
        self.assertEqual(result["7/4"], "Independence Day")

    def test_failure1(self):
        # Mock the requests.get method to return a failed response
        requests = Mock()
        requests.get.return_value.status_code = 404

        # Test that the get_holidays function returns None when the response is not successful
        with unittest.mock.patch("calendar3.requests", requests):
            result = calendar3.get_holidays()
        self.assertIsNone(result)

#
# 100%
#