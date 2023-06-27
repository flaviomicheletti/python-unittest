from unittest.mock import patch


class MyClass:
    def add(self, a, b):
        return a + b


# Patch the add method of MyClass with a mock
with patch.object(MyClass, 'add') as mock_add:
    # Set the return value of the mock
    mock_add.return_value = 100

    # Create an instance of MyClass
    my_instance = MyClass()

    # Call the patched add method
    result = my_instance.add(10, 20)

    # Verify the mock was called
    assert mock_add.called

    # Verify the mock was called with the correct arguments
    mock_add.assert_called_with(10, 20)

    # Verify the result
    assert result == 100
