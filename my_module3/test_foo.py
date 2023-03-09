# test_my_module.py
import unittest
from unittest.mock import MagicMock, patch
from my_module3 import MyClass


class TestMyClass(unittest.TestCase):
    def test_get_data_success(self):
        expected_data = {"name": "John Doe", "age": 30}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data

        with patch("requests.get", return_value=mock_response) as mock_get:
            my_class = MyClass("http://example.com")
            data = my_class.get_data()

            mock_get.assert_called_once_with("http://example.com")
            self.assertEqual(data, expected_data)

    def test_get_data_failure(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 404

            my_class = MyClass("http://example.com")
            data = my_class.get_data()

            mock_get.assert_called_once_with("http://example.com")
            self.assertIsNone(data)
