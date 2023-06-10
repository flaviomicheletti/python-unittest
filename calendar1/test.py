import unittest
from datetime import datetime
from unittest.mock import patch
from calendar1 import is_weekday


class TestIsWeekday(unittest.TestCase):
    @patch('calendar1.datetime')
    def test_weekday(self, mock_datetime):
        # Create a datetime object for a Monday
        mock_datetime.today.return_value.weekday.return_value = 0
        self.assertTrue(is_weekday())

    @patch('calendar1.datetime')
    def test_saturday(self, mock_datetime):
        # Create a datetime object for a Saturday
        mock_datetime.today.return_value.weekday.return_value = 5
        self.assertFalse(is_weekday())

    @patch('calendar1.datetime')
    def test_sunday(self, mock_datetime):
        # Create a datetime object for a Sunday
        mock_datetime.today.return_value.weekday.return_value = 6
        self.assertFalse(is_weekday())

    @patch('calendar1.datetime')
    def test_friday(self, mock_datetime):
        # Create a datetime object for a Friday
        mock_datetime.today.return_value.weekday.return_value = 4
        self.assertTrue(is_weekday())


if __name__ == '__main__':
    unittest.main()
