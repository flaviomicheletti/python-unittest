import unittest
from unittest import mock
from api2 import get_holidays

class TestGetHolidays(unittest.TestCase):

    @mock.patch('api2.requests.get')
    def test_get_holidays_success(self, mock_get):
        # Prepare the mock response
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'holidays': ['New Year', 'Christmas']}
        mock_get.return_value = mock_response

        # Call the function
        result = get_holidays()

        # Assert the expected behavior
        self.assertEqual(result, {'holidays': ['New Year', 'Christmas']})
        mock_get.assert_called_once_with("http://localhost/api/holidays")

    @mock.patch('api2.requests.get')
    def test_get_holidays_failure(self, mock_get):
        # Prepare the mock response
        mock_response = mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the function
        result = get_holidays()

        # Assert the expected behavior
        self.assertIsNone(result)
        mock_get.assert_called_once_with("http://localhost/api/holidays")

#
# 100%
#