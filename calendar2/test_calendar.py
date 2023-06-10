import unittest
from datetime import datetime
# how to avoid the line bellow?
# from calendar2 import str2date, get_month, get_month_abbr, get_weekday, get_weekday_abbr, parse_date, enhance_event_date_info
# from calendar2 import *
import calendar2


class TestCalendar2(unittest.TestCase):
    def test_str2date(self):
        # Test case 1: Valid date string
        input_str = '2023-06-10 12:00:00'
        expected_output = datetime(2023, 6, 10, 12, 0, 0)
        assert calendar2.str2date(input_str) == expected_output

        # Test case 2: Invalid date string
        input_str = '2023-13-40 25:70:00'
        # In this case, the function should raise a ValueError
        try:
            calendar2.str2date(input_str)
        except ValueError:
            assert True
        else:
            assert False, "Expected ValueError was not raised"

    def test_get_month(self):
        # Test case 1: January
        input_date = datetime(2023, 1, 15)
        expected_output = 'January'
        assert calendar2.get_month(input_date) == expected_output

        # Test case 2: December
        input_date = datetime(2023, 12, 31)
        expected_output = 'December'
        assert calendar2.get_month(input_date) == expected_output

    def test_get_month_abbr(self):
        # Test case 1: January
        input_date = datetime(2023, 1, 15)
        expected_output = 'Jan'
        assert calendar2.get_month_abbr(input_date) == expected_output

        # Test case 2: December
        input_date = datetime(2023, 12, 31)
        expected_output = 'Dec'
        assert calendar2.get_month_abbr(input_date) == expected_output

    def test_get_weekday(self):
        # Test case 1: Monday
        input_date = datetime(2023, 6, 12)
        expected_output = 'Monday'
        assert calendar2.get_weekday(input_date) == expected_output

        # Test case 2: Sunday
        input_date = datetime(2023, 6, 18)
        expected_output = 'Sunday'
        assert calendar2.get_weekday(input_date) == expected_output

    def test_get_weekday_abbr(self):
        # Test case 1: Monday
        input_date = datetime(2023, 6, 12)
        expected_output = 'Mon'
        assert calendar2.get_weekday_abbr(input_date) == expected_output

        # Test case 2: Sunday
        input_date = datetime(2023, 6, 18)
        expected_output = 'Sun'
        assert calendar2.get_weekday_abbr(input_date) == expected_output

    def test_parse_date(self):
        # Test case 1: Valid date string
        input_str = '2023-06-10 12:00:00'
        expected_output = datetime(2023, 6, 10, 12, 0, 0)
        assert calendar2.parse_date(input_str) == expected_output

        # Test case 2: Invalid date string
        input_str = 'invalid_date'
        expected_output = datetime(1970, 1, 1, 0, 0, 0)
        assert calendar2.parse_date(input_str) == expected_output

    def test_enhance_event_date_info(self):
        # Test case 1: Valid event dictionary with a valid date
        event = {
            'event_date': '2023-06-10 12:30:00',
            'other_key': 'other_value'
        }
        expected_output = {
            'event_date': '2023-06-10 12:30:00',
            'other_key': 'other_value',
            'month': 'June',
            'month_abbr': 'Jun',
            'weekday': 'Saturday',
            'weekday_abbr': 'Sat',
            'year': 2023,
            'day': 10,
            'time': '12:30 PM'
        }
        self.assertEqual(calendar2.enhance_event_date_info(
            event),  expected_output)

        # Test case 2: Valid event dictionary with an invalid date
        event = {
            'event_date': 'invalid_date',
            'other_key': 'other_value'
        }
        expected_output = {
            'event_date': 'invalid_date',
            'other_key': 'other_value',
            'month': 'January',
            'month_abbr': 'Jan',
            'weekday': 'Thursday',
            'weekday_abbr': 'Thu',
            'year': 1970,
            'day': 1,
            'time': '12:00 AM'
        }

        self.assertEqual(calendar2.enhance_event_date_info(event), expected_output)
