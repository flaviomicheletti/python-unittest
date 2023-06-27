from unittest.mock import Mock

# Create a mock object
my_mock = Mock()

# Set a return value for the mock
my_mock.return_value = 42

# Call the mock
result = my_mock(10, 20)
assert result == 42

# Verify the mock was called
assert my_mock.called

# Verify the mock was called with specific arguments
my_mock.assert_called_with(10, 20)

# Reset the mock's state
my_mock.reset_mock()

# Verify the mock was not called again after reset
assert not my_mock.called
