import unittest
from unittest.mock import Mock
from calculator2 import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        mock_calculator = Mock(Calculator)
        mock_calculator.add.return_value = 3
        result = mock_calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        mock_calculator = Mock(Calculator)
        mock_calculator.subtract.return_value = -1
        result = mock_calculator.subtract(1, 2)
        self.assertEqual(result, -1)

    def test_multiply(self):
        mock_calculator = Mock(Calculator)
        mock_calculator.multiply.return_value = 2
        result = mock_calculator.multiply(1, 2)
        self.assertEqual(result, 2)

    def test_divide(self):
        mock_calculator = Mock(Calculator)
        mock_calculator.divide.return_value = 2
        result = mock_calculator.divide(4, 2)
        self.assertEqual(result, 2)


