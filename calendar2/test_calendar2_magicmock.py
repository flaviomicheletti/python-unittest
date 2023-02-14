import unittest
from unittest.mock import MagicMock
import requests
import calendar2


class TestMagicMock(unittest.TestCase):
    def test_get_data(self):

        actual = {"foo": "lish"}

        # Set up the mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = actual

        # Create a mock object for the requests.get method
        mock = MagicMock()
        mock.return_value = mock_response

        # Replace the requests.get method with the mock object
        requests.get = mock

        # Call the function under test
        result = calendar2.get_data()

        # Assert that the function returns the expected result
        self.assertEqual(result, actual)

        # Assert that the requests.get method was called with the expected URL
        mock.assert_called_once_with("http://localhost/api/holidays")
