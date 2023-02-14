import unittest
from unittest.mock import Mock, patch
import client1


class TestAPIClient(unittest.TestCase):
    @patch("client1.requests")
    def test_get(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_requests.get.return_value = mock_response

        client = client1.APIClient("http://example.com")
        result = client.get("endpoint")
        self.assertEqual(result, {"key": "value"})


