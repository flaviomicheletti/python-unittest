import requests
import unittest
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):
    def response_mock(self, url):
        # Log a fake request for test output purposes
        # print(f'Making a request to {url}.')
        # print('Request received!')

        # Create a new Mock to imitate a Response
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.response_mock
        actual = get_holidays()
        assert actual["12/25"] == "Christmas"
