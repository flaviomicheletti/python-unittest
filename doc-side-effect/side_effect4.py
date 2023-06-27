import unittest
from unittest.mock import Mock


def divide(a, b):
    return a / b


class MyTestCase(unittest.TestCase):
    def test_divide(self):
        # Create a mock object for the 'divide' function
        mock_divide = Mock()

        # Define the desired behavior using side_effect
        mock_divide.side_effect = lambda x, y: x + y

        # Replace the original 'divide' function with the mock
        with unittest.mock.patch('__main__.divide', mock_divide):
            # Call the code under test
            result = divide(4, 2)

            # Assert the expected behavior
            self.assertEqual(result, 6)

        # Simulating a side effect of raising an exception
        mock_divide.side_effect = ValueError("Custom error")
        with self.assertRaises(ValueError):
            mock_divide(10, 0)


if __name__ == '__main__':
    unittest.main()
