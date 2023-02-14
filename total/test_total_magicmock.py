import unittest
from unittest.mock import MagicMock
import total


class TestTotalMock(unittest.TestCase):
    def test_calculate_total(self):
        total.read = MagicMock()
        total.read.return_value = [1, 2, 3]
        result = total.calculate_total("")
        self.assertEqual(result, 6)

