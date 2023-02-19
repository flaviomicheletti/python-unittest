import unittest
from requests.exceptions import Timeout
from unittest.mock import patch
from calendar1 import get_holidays


class TestCalendar(unittest.TestCase):
    @patch("calendar1.requests")
    def test_get_holidays_timeout(self, mock):
        
        mock.get.side_effect = Timeout

        with self.assertRaises(Timeout):
            get_holidays()
            mock.get.assert_called_once()


