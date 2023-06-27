from unittest.mock import patch
import math


def calculate_square_root(number):
    return math.sqrt(number)


# Patch the math.sqrt function with a mock
with patch('math.sqrt') as mock_sqrt:
    # Set the return value of the mock
    mock_sqrt.return_value = 5.0

    # Call the function that uses math.sqrt
    result = calculate_square_root(25)

    # Verify the mock was called
    assert mock_sqrt.called

    # Verify the mock was called with the correct argument
    mock_sqrt.assert_called_with(25)

    # Verify the result
    assert result == 5.0
