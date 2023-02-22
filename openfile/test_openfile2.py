import unittest
from unittest.mock import mock_open, patch


def my_open1(filename, mode):
    result = open(filename, "r")
    return result


class TestMyOpen(unittest.TestCase):
    def test_my_open(self):
        filename = "test_file.txt"
        expected_result = "test data"

        # Create a mock object that returns the expected result
        mock_file = mock_open(read_data=expected_result)

        # Patch the built-in `open()` function with the mock object
        with patch("builtins.open", mock_file):
            # Call the `my_open1()` function
            result = my_open1(filename, "r")

            # Verify that the expected result was returned
            self.assertEqual(result.read(), expected_result)

        # Verify that the `open()` function was called with the correct arguments
        mock_file.assert_called_once_with(filename, "r")
