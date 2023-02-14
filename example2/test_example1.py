import unittest
from unittest.mock import Mock, patch

def get_data(url):
    import requests
    return requests.get(url).json()

class TestGetData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_with_mock(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'data': 'mocked data'}
        mock_get.return_value = mock_response

        result = get_data('http://test.com/data')

        mock_get.assert_called_with('http://test.com/data')
        mock_response.json.assert_called_once()
        self.assertEqual(result, {'data': 'mocked data'})
