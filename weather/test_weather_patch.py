import unittest
from unittest.mock import patch
from weather import get_weather_data


class TestGetWeatherData(unittest.TestCase):
    @patch("weather.requests.get")
    def test_get_weather_data(self, mock_get):
        actual = 273.15
        mock_response = {"main": {"temp": actual}}
        mock_get.return_value.json.return_value = mock_response
        expected = get_weather_data("London")
        self.assertEqual(expected, actual)


