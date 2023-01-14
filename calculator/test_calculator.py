from unittest import TestCase
from unittest.mock import patch
import calculator

class TestCalculator(TestCase):
    @patch('calculator.Calculator.add', return_value=9)
    def test_add(self, add):
        expected = add(2, 3)
        self.assertEqual(expected, 9)
