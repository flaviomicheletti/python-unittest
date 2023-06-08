import unittest
from unittest.mock import MagicMock
import total


class TestTotalMock(unittest.TestCase):
    def test_calculate_total(self):

        tmp = total.read

        total.read = MagicMock()
        total.read.return_value = [1, 2, 3]

        actual = total.calculate("fake-filename")
        self.assertEqual(actual, 6)

        """You need to be careful to restore the original
        state of the function, otherwise it would modify 
        the 'test_read' file"""
        total.read = tmp

#
# 57%
#