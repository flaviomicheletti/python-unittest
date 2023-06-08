import unittest
from unittest.mock import MagicMock, patch
import total


class TestTotalMock(unittest.TestCase):

    @patch('builtins.open')
    def test_read(self, mock_open):
        # Set up the mock file object
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.readlines.return_value = ['1.0\n', '2.5\n', '3.7\n']

        # Configure the mock open function to return the mock file object
        mock_open.return_value = mock_file

        # Call the read function with a dummy filename
        result = total.read('dummy.txt')

        # Assert the expected result
        self.assertEqual(result, [1.0, 2.5, 3.7])
        # self.assertEqual(result, [1, 2, 3])

#
# 71%
#