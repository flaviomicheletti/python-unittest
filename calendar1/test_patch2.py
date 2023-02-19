import requests
import unittest
from unittest.mock import patch
from calendar1 import get_holidays

class TestCalendar(unittest.TestCase):
    @patch.object(requests, "get", side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, foo):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()
