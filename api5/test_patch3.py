import unittest
from unittest.mock import MagicMock
from api5 import get_weather_data


class TestGetWeatherData(unittest.TestCase):
    def test_get_weather_data(self):
        actual = 273.15

        mock_response = MagicMock()
        mock_response.json.return_value = {"main": {"temp": actual}}
        mock = MagicMock(return_value=mock_response)
        
        with unittest.mock.patch("api5.requests.get", new=mock):
            expected = get_weather_data("London")
            self.assertEqual(expected, actual)

#
# 100% 
#