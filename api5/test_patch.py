import unittest
from unittest.mock import patch
from api5 import get_weather_data


class TestGetWeatherData(unittest.TestCase):
    @patch("api5.requests.get")
    def test_get_weather_data(self, mock):
        actual = 273.15

        mock.return_value.json.return_value = {"main": {"temp": actual}}

        expected = get_weather_data("London")
        self.assertEqual(expected, actual)

#
# 100%
#
