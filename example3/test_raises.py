import unittest


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_valid(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
