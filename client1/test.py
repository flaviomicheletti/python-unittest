import unittest
from unittest.mock import Mock, patch
import client1


class TestAPIClient(unittest.TestCase):
    @patch("client1.requests")
    def test_get(self, mock_requests):
        expected = {"key": "value"}

        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_requests.get.return_value = mock_response

        api = client1.Api("http://example.com")
        actual = api.get("endpoint")
        self.assertEqual(actual, expected)


