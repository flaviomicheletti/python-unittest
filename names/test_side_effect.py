import unittest
from unittest.mock import MagicMock

import requests
from names import fetch_data


class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        # Define mock response
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {'name': 'John'},
            {'name': 'Jane'},
            {'name': 'Bob'}
        ]

        # Set side_effect of requests.get to return mock response
        requests.get.side_effect = lambda url: mock_response

        # Call the fetch_data function with a mock URL
        data = fetch_data('http://example.com/data')

        # Verify that the function returned the expected data
        self.assertEqual(data, ['John', 'Jane', 'Bob'])


if __name__ == '__main__':
    unittest.main()
