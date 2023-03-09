import unittest
from unittest.mock import Mock, patch

def get_data(url):
    import requests
    return requests.get(url).json()

class TestGetData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_with_mock(self, requests_mock):
        mock_response = Mock()
        mock_response.json.return_value = {'data': 'mocked data'}
        requests_mock.return_value = mock_response

        actual = get_data('http://test.com/data')
        self.assertEqual(actual, {'data': 'mocked data'})

        requests_mock.assert_called_with('http://test.com/data')
        mock_response.json.assert_called_once()
