import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()


def get_holidays():
    response = requests.get("http://localhost/api/holidays")
    if response.status_code == 200:
        return response.json()
    # try:
    #     response = requests.get("http://localhost/api/holidays")
    #     if response.status_code == 200:
    #         return response.json()
    # except:
    #     return {}


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
