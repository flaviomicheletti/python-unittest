from unittest.mock import Mock

# Create a mock object with a side effect
my_mock = Mock(side_effect=lambda x, y: x * y)

# Call the mock with arguments
result = my_mock(10, 5)

# Access the call arguments
args = my_mock.call_args
arg1, arg2 = args[0]

assert result == 50
assert arg1 == 10
assert arg2 == 5
