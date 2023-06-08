from unittest.mock import Mock

# Create mock objects for the add and multiply methods
mock_add = Mock()
mock_multiply = Mock()

# Set side effects for the methods
mock_add.side_effect = lambda a, b: a + b
mock_multiply.side_effect = lambda a, b: a * b

# Perform calculations
result1 = mock_add(5, 10)
mock_add.assert_called_with(5, 10)

result2 = mock_multiply(result1, 3)
mock_multiply.assert_called_with(result1, 3)

# Verify call order of method calls
call_order = mock_add.mock_calls + mock_multiply.mock_calls
assert call_order == [mock_add.call_args, mock_multiply.call_args]
