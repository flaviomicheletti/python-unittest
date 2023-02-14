import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock
from calendar1 import get_holidays


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        """ Test a connection timeout """
        get_holidays = Mock()
        get_holidays.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
