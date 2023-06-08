# Mock vs Patch

What would be the difference between unittest.mock.Mock and 
unittest.mock.patch? When should I use one and when should I use the other? 
Maybe I should use both together? 

`unittest.mock.Mock` and `unittest.mock.patch` are both part of the `
unittest.mock` module in Python's standard library, which provides a powerful 
way to mock objects and control their behavior during testing. Here's the 
difference between the two: 

1. `unittest.mock.Mock`: `Mock` is a class that allows you to create mock 
objects with customizable behavior. You can define return values, side 
effects, and assertions on method calls. Mock objects created with `Mock` are 
primarily used to replace dependencies or simulate objects that are difficult 
or time-consuming to create for testing purposes. 

2. `unittest.mock.patch`: `patch` is a context manager and a decorator 
provided by the `unittest.mock` module. It's used to temporarily replace 
objects or attributes with mock objects within a specific scope, such as a 
test function or a test case. When used as a decorator, `patch` automatically 
applies the patching for the duration of the decorated function. When used as 
a context manager, you manually specify the scope of patching using the `
with` statement. 

## Now, when to use each of them: 

- `Mock` is useful when you want to create individual mock objects with 
specific behaviors that you need throughout your tests. You typically use `
Mock` to replace dependencies or simulate complex behavior in isolated units 
of code. 

- `patch` is handy when you want to temporarily replace objects or attributes 
in a broader scope, such as a module or class, for the duration of a test 
case or a test function. It allows you to patch multiple objects or 
attributes at once, making it convenient for testing interactions between 
different parts of your codebase. 

In some cases, you may use both `Mock` and `patch` together. For example, you 
could create a `Mock` object with specific behavior and then use `patch` to 
replace an attribute or method on an object with that `Mock` object. This 
allows you to control the behavior of the patched object while keeping the 
flexibility of `Mock` for other purposes within your test. 

Here's an example to illustrate the combined usage:

```python
from unittest.mock import Mock, patch

class MyClass:
    def method(self):
        return "Original"

# Using Mock and patch together
def test_my_function():
    mock_obj = Mock(return_value="Mocked")
    with patch.object(MyClass, 'method', mock_obj):
        obj = MyClass()
        assert obj.method() == "Mocked"

    # `obj.method` is now restored to its original behavior
    obj = MyClass()
    assert obj.method() == "Original"
```

In this example, `Mock` is used to create a mock object with a custom return 
value ("Mocked"), and `patch` is used to temporarily replace the `method` of `
MyClass` with the `mock_obj`. This allows you to control the behavior of `
MyClass.method` within the scope of the test function. Once the `with` block 
is exited, the original behavior of `MyClass.method` is restored. 

Overall, `Mock` and `patch` are both powerful tools for test mocking, but 
their usage depends on the specific needs and scope of your testing 
scenarios. 


## More details

Here's some additional information to further understand 
the usage of `unittest.mock.Mock` and `unittest.mock.patch`:

1. `unittest.mock.Mock`:

- `Mock` objects are highly configurable and can be used to simulate the 
behavior of real objects or functions. They allow you to set return values, 
side effects (such as raising exceptions), and define assertions on method 
calls. 

- `Mock` objects have attributes and methods that allow you to inspect their 
usage, such as `called` (whether the mock has been called), `call_count` (the 
number of times it was called), `assert_called_with()` (verifying specific 
arguments), etc. 

- `Mock` objects are often used as placeholders for dependencies or to 
simulate complex behavior in isolation during unit testing. 

Here's an example of using `Mock`:

```python
from unittest.mock import Mock

# Create a Mock object
mock_obj = Mock()
mock_obj.method.return_value = 42

# Test using the mock object
result = mock_obj.method(1, 2, 3)
assert result == 42
assert mock_obj.method.call_count == 1
mock_obj.method.assert_called_with(1, 2, 3)
```

In this example, `mock_obj` is a `Mock` object that is configured to return `
42` when the `method` is called. We can then assert the return value, the 
number of times the method was called, and the arguments it was called with. 

2. `unittest.mock.patch`:

- `patch` is used to temporarily replace objects or attributes with mock 
objects. It can be applied as a decorator or a context manager, and it 
automatically manages the patching and cleanup of objects. 

- `patch` allows you to patch objects at different levels, such as replacing 
an attribute of an object, a module-level attribute, or even built-in 
functions. 

- The patching takes effect only within the specified scope, typically a test 
function or a test case. Once the scope is exited, the original objects or 
attributes are restored. 

Here's an example of using `patch`:

```python
from unittest.mock import patch

def my_function():
    return "Original"

# Using patch as a decorator
@patch('__main__.my_function')
def test_my_function(mock_func):
    mock_func.return_value = "Mocked"
    result = my_function()
    assert result == "Mocked"
    mock_func.assert_called_once()

# Using patch as a context manager
def test_my_function():
    with patch('__main__.my_function') as mock_func:
        mock_func.return_value = "Mocked"
        result = my_function()
        assert result == "Mocked"
        mock_func.assert_called_once()
```

In both examples, `patch` is used to temporarily replace `my_function` with a 
mock object. The mock object is then configured to return `"Mocked"`. Within 
the scope of the test, the function behaves as expected with the patched 
behavior. 

Using `unittest.mock.Mock` and `unittest.mock.patch` together allows you to 
combine the flexibility of creating custom mock objects with the ability to 
temporarily replace objects or attributes during testing. This combination is 
particularly useful when you need to control the behavior of specific objects 
or attributes while keeping the rest of your code intact. 
