from unittest.mock import Mock


class Calculator:
    def __init__(self):
        self.total = 0

    def add(self, number):
        self.total += number

    def multiply(self, number):
        self.total *= number


# Create an instance of the Calculator class
calculator = Calculator()

# Create a mock object for the add method
mock_add = Mock()

# Patch the add method with the mock
calculator.add = mock_add

# Call the add method with arguments
calculator.add(5)
# Verify the add method was called with specific arguments
mock_add.assert_called_with(5)

calculator.add(10)
# Verify the add method was called with specific arguments
mock_add.assert_called_with(10)

calculator.add(15)
# Verify the add method was called with specific arguments
mock_add.assert_called_with(15)

# Verify the add method was called three times
# print( mock_add.call_count)
assert mock_add.call_count == 3

# Access the call arguments for each call
args_list = mock_add.call_args_list
expected_arguments = [5, 10, 15]

for i, args in enumerate(args_list):
    number = args[0][0]
    assert number == expected_arguments[i]


# Reset the mock's call count
mock_add.reset_mock()

# Verify the add method was not called after reset
assert mock_add.call_count == 0
