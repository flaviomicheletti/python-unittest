from unittest import TestCase
from unittest.mock import patch
import calculator


class TestCalculator(TestCase):
    @patch("calculator.add", return_value=9)
    def test_add(self, add):
        expected = add(5, 5)
        self.assertEqual(expected, 9)


def mock_add(x, y):
    return 11


class TestCalculatorSideEffect(TestCase):
    @patch("calculator.add", side_effect=mock_add)
    def test_add(self, add):
        expected = add(5, 5)
        self.assertEqual(expected, 11)
