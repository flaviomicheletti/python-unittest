import unittest
from unittest.mock import patch
import total


class TestTotalPatch(unittest.TestCase):
    @patch("total.read")
    def test_calculate_total(self, mock_read):
        mock_read.return_value = [1, 2, 3]
        result = total.calculate_total("")
        self.assertEqual(result, 6)
