import unittest
from unittest.mock import Mock
import calendar2


class TestCalendar(unittest.TestCase):
    def test_get_data_success(self):
        # Mock the requests.get method to return a successful response
        mock = Mock()
        mock.get.return_value.status_code = 200
        mock.get.return_value.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }

        # Temporarily replace the requests.get method with the mocked version
        original = calendar2.requests.get
        calendar2.requests.get = mock.get

        # Test that the get_data function returns the expected actual
        actual = calendar2.get_data()
        self.assertEqual(actual["12/25"], "Christmas")
        self.assertEqual(actual["7/4"], "Independence Day")

        # Restore the original requests.get method
        calendar2.requests.get = original

    def test_get_data_failure(self):
        # Mock the requests.get method to return a failed response
        requests = Mock()
        requests.get.return_value.status_code = 404

        # Temporarily replace the requests.get method with the mocked version
        original = calendar2.requests.get
        calendar2.requests.get = requests.get

        # Test that the get_data function returns None when the response is not successful
        actual = calendar2.get_data()
        self.assertIsNone(actual)

        # Restore the original requests.get method
        calendar2.requests.get = original
