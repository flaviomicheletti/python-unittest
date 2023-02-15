import unittest
from unittest.mock import patch
import total


class TestTotalPatch(unittest.TestCase):
    @patch("total.read")
    def test_calculate_total(self, mock):
        mock.return_value = [1, 2, 3]

        actual = total.calculate_total("fake-filename")
        self.assertEqual(actual, 6)
