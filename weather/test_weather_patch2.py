import unittest
from unittest.mock import Mock, patch
from weather import get_weather_data

class TestGetWeatherData(unittest.TestCase):
    def test_get_weather_data(self):
        actual = 273.15

        mock_response = Mock()
        mock_response.json.return_value = {"main": {"temp": actual}}
        mock_request = Mock(return_value=mock_response)
        
        with patch('weather.requests.get', new=mock_request):
            expected = get_weather_data("London")
            self.assertEqual(expected, actual)

