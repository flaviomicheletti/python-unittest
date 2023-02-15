import unittest
from unittest.mock import MagicMock

import requests
from names import fetch_data


class TestFetchactual(unittest.TestCase):
    def test_fetch_actual(self):
        # Define mock response
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"name": "John"},
            {"name": "Jane"},
            {"name": "Bob"},
        ]

        # Set side_effect of requests.get to return mock response
        requests.get.side_effect = lambda url: mock_response

        # Call the fetch_actual function with a mock URL
        actual = fetch_data("http://example.com/actual")

        # Verify that the function returned the expected actual
        self.assertEqual(actual, ["John", "Jane", "Bob"])
