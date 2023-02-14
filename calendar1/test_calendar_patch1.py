import unittest
from requests.exceptions import Timeout
from unittest.mock import patch
from calendar1 import get_holidays


class TestCalendar(unittest.TestCase):
    @patch("calendar1.requests")
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


