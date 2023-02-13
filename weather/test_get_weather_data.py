import unittest
from unittest.mock import patch
from weather import get_weather_data


class TestGetWeatherData(unittest.TestCase):
    @patch("weather.requests.get")
    def test_get_weather_data(self, mock_get):
        number = 273.15
        actual = {"main": {"temp": number}}
        mock_get.return_value.json.return_value = actual
        expected = get_weather_data("London")
        self.assertEqual(expected, number)


