from unittest import TestCase
from unittest.mock import patch
# from calculator1 import add


class TestCalculator(TestCase):
    @patch("calculator1.add", return_value=9)
    def test_add(self, mock):
        self.assertEqual(mock(5, 5), 9)


def mock_add(x, y):
    return 11


class TestCalculatorSideEffect(TestCase):
    @patch("calculator1.add", side_effect=mock_add)
    def test_add(self, mock):
        self.assertEqual(mock(5, 5), 11)

#
# 50%
#