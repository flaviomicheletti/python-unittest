import unittest
from unittest.mock import MagicMock
from weather import get_weather_data


class TestGetWeatherData(unittest.TestCase):
    def test_get_weather_data(self):
        mock_response = MagicMock()
        actual = 273.15
        mock_response.json.return_value = {"main": {"temp": actual}}
        mock_request = MagicMock(return_value=mock_response)
        with unittest.mock.patch("weather.requests.get", new=mock_request):
            expected = get_weather_data("London")
            self.assertEqual(expected, actual)
