import unittest
from unittest.mock import MagicMock
import requests
from weather import get_weather_data


class TestGetData(unittest.TestCase):
    def test_get_data(self):

        actual = 273.15

        # Set up the mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {"main": {"temp": actual}}

        # Create a mock object for the requests.get method
        mock_get = MagicMock()
        mock_get.return_value = mock_response

        # Replace the requests.get method with the mock object
        requests.get = mock_get

        # Call the function under test
        result = get_weather_data("scs")

        # Assert that the function returns the expected result
        self.assertEqual(result, actual)

        # Assert that the requests.get method was called with the expected URL
        mock_get.assert_called_once_with(
            "https://api.openweathermap.org/data/2.5/weather?q=scs&appid=API_KEY"
        )
