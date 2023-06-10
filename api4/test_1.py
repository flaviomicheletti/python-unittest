import unittest
from unittest.mock import Mock, patch
from api4 import fetch_data

class FetchDataTestCase(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Mock the response from the API
        mock_response = Mock()
        mock_response.json.return_value = [
            {'name': 'Item 1'},
            {'name': 'Item 2'},
            {'name': 'Item 3'}
        ]
        mock_get.return_value = mock_response

        # Call the function with a mock URL
        url = 'http://example.com/data'
        result = fetch_data(url)

        # Assert the expected output
        expected_result = ['Item 1', 'Item 2', 'Item 3']
        self.assertEqual(result, expected_result)

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with(url)
