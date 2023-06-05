# Unittest mocks

Unittest is a popular testing framework in Python that provides various ways to 
create mock objects to replace real objects in your tests. Using mock objects 
helps isolate the code under test and ensures that external dependencies, like 
databases or APIs, do not affect test results. Here are some of the ways to 
create mocks using unittest in Python:

## unittest.mock.Mock:

The most basic way to create a mock object. You can use the `Mock` class to 
replace the target object and define custom behavior for its methods or attributes.

``` Python
from unittest.mock import Mock

mocked_object = Mock()
mocked_object.some_method.return_value = 'some_value'
```

## unittest.mock.MagicMock: 

A subclass of Mock that includes most of the magic methods (e.g., 
`__getitem__`, `__iter__`, etc.). Use this when you need your mock object to 
behave like a container or support other magic methods.


``` Python
from unittest.mock import MagicMock

magic_mocked_object = MagicMock()
magic_mocked_object.__getitem__.return_value = 'item_value'
```

## unittest.mock.patch: 

A context manager or decorator that temporarily replaces the specified object 
with a `Mock` or `MagicMock` during the test. This is useful when you want to 
replace a function or a class in the module you're testing.

``` Python
from unittest.mock import patch

# As a context manager
with patch('module_under_test.ClassName') as MockedClass:
    mocked_instance = MockedClass.return_value
    mocked_instance.method.return_value = 'mocked_value'

# As a decorator
@patch('module_under_test.ClassName')
def test_function(MockedClass):
    mocked_instance = MockedClass.return_value
    mocked_instance.method.return_value = 'mocked_value'
```

## unittest.mock.patch.object:

A context manager or decorator that temporarily replaces a specific attribute 
of an object with a `Mock` or `MagicMock`. This is useful when you want to replace 
a method or attribute of a class or an instance.

``` Python
from unittest.mock import patch

# As a context manager
with patch.object(module_under_test.ClassName, 'method_name') as mocked_method:
    mocked_method.return_value = 'mocked_value'

# As a decorator
@patch.object(module_under_test.ClassName, 'method_name')
def test_function(mocked_method):
    mocked_method.return_value = 'mocked_value'
```

## unittest.mock.patch.multiple:

A context manager or decorator that allows you to patch multiple attributes of 
an object simultaneously.

``` Python
from unittest.mock import patch

# As a context manager
with patch.multiple(module_under_test.ClassName, attr1=Mock(), attr2=Mock()) as mocked_attrs:
    pass

# As a decorator
@patch.multiple(module_under_test.ClassName, attr1=Mock(), attr2=Mock())
def test_function():
    pass
```

## unittest.mock.PropertyMock: 

A mock for class or instance properties. This can be used in conjunction with 
`patch.object` to replace a property with a mock.

``` Python
from unittest.mock import PropertyMock, patch

class MyClass:
    @property
    def my_property(self):
        return 'real_value'

# As a context manager
with patch.object(MyClass, 'my_property', new_callable=PropertyMock) as mocked_property:
    mocked_property.return_value = 'mocked_value'

# As a decorator
@patch.object(MyClass, 'my_property', new_callable=PropertyMock)
def test_function(mocked_property):
    mocked_property.return_value = 'mocked_value'
```




# with specific arguments

These are the primary ways to create mocks using unittest in Python. Depending
on your test requirements, you can also configure these mock objects to assert 
that they were called with specific arguments, count the number of calls, or 
even raise exceptions.

Here are some common ways to configure mock objects:

## return_value: 

Set a return value for the mock object when it's called.

``` Python
mocked_function.return_value = 'mocked_value'
```

## side_effect: 

Set a function or an exception as a side effect. If a function is provided, 
it will be called with the same arguments as the mock, and the result will be 
the mock's return value. If an exception is provided, it will be raised when 
the mock is called.

``` Python
# Using a function
def side_effect_function(*args, **kwargs):
    return 'side_effect_value'

mocked_function.side_effect = side_effect_function

# Using an exception
mocked_function.side_effect = Exception('error_message')
```

## assert_called_once_with: 

Assert that the mock was called exactly once with the specified arguments.

``` Python
mocked_function.assert_called_once_with(arg1, arg2)
```

## assert_called_with:

Assert that the mock was last called with the specified arguments.

``` Python
mocked_function.assert_called_with(arg1, arg2)
```

## assert_any_call: 

Assert that the mock was called with the specified arguments at least once.

``` Python
mocked_function.assert_any_call(arg1, arg2)
```

## call_count: 

Check the number of times the mock was called.

``` Python
assert mocked_function.call_count == 2
```

## call_args: 

Check the arguments of the last call to the mock.

``` Python
assert mocked_function.call_args == ((arg1, arg2),)
```

## call_args_list: 

Check the arguments of all calls to the mock.

``` Python
assert mocked_function.call_args_list == [((arg1, arg2),), ((arg3, arg4),)]
```

These methods and attributes provide you with various ways to configure mock 
objects and verify their interactions in your tests. With unittest and its 
mock capabilities, you can efficiently create isolated and deterministic tests 
for your Python code.



# advanced features

In addition to the methods and attributes mentioned earlier, there are even 
more advanced features and techniques available in the unittest.mock module to 
help you customize and manage your mock objects for various testing scenarios.

## reset_mock: 

Resets the call count, call arguments, and child mocks of a mock object. 
This is useful when you want to reuse a mock object across different parts of 
a test or across multiple tests.

``` Python
mocked_function.reset_mock()
```

## configure_mock: 

Configure a mock object's attributes and behavior in a single call using 
keyword arguments.

``` Python
mocked_object.configure_mock(attr1='value1', attr2='value2', method=Mock(return_value='method_value'))
```

## spec: 

Provide a specification for the mock object by passing an existing object or 
a list of attributes. This ensures that the mock object only has the same 
attributes as the specified object or the provided list.

``` Python
# Using an existing object
mocked_object = Mock(spec=real_object)

# Using a list of attributes
mocked_object = Mock(spec=['attr1', 'attr2'])
```

## spec_set: 

Similar to spec, but it also prevents the mock object from having new attributes assigned to it.

``` Python
# Using an existing object
mocked_object = Mock(spec_set=real_object)

# Using a list of attributes
mocked_object = Mock(spec_set=['attr1', 'attr2'])
```

## wraps: 

Wrap an existing object with a mock, such that when the mock is called, it 
calls the original object's method and returns its result. This is useful 
when you want to keep the original behavior but still track calls or add 
side effects.

``` Python
mocked_function = Mock(wraps=real_function)
```

## mock_open: 

A helper function to create a mock for the open function. This is useful when 
you want to mock file I/O operations.

``` Python
from unittest.mock import mock_open, patch

m = mock_open(read_data='file_content')
with patch('builtins.open', m):
    # Test code that reads from a file
    pass
```

## ANY: 

A special constant that can be used in assertions to indicate that you don't 
care about the exact value of an argument.

``` Python
from unittest.mock import ANY

mocked_function.assert_called_with(ANY, 'specific_arg')
```

These advanced features of the unittest.mock module enable you to handle more 
complex testing scenarios and requirements. By combining and customizing these 
features, you can create powerful and flexible tests that can help you 
validate the correctness of your Python code.


# best practices and tips

Alongside the features already mentioned, it's essential to understand some 
best practices and tips for using the unittest.mock module effectively. 

## Keep tests simple and focused: 

Test only one specific behavior or functionality at a time. This makes your 
tests easier to understand, maintain, and debug. 

## Don't over-mock: 

Only mock the parts of your code that involve external dependencies, 
randomness, or time-consuming operations. Avoid mocking everything, as this 
can make your tests less effective in catching real-world issues. 

## Use `patch` for proper cleanup: 

Whenever possible, use the patch context manager or decorator to replace 
objects during tests, as this ensures that the original objects are 
restored after the test is done. This can help avoid issues related to 
global state and side effects. 

## Combine mock objects when necessary: 

You can create mock objects that have other mock objects as attributes, 
allowing you to test complex interactions between multiple objects. 
However, avoid making these structures overly complex, as it can make your 
tests harder to understand and maintain. 

## Check mock object interactions: 

Use the various assert methods provided by Mock objects to verify that they 
were called with the expected arguments and the correct number of times. 
This helps ensure that your code is interacting with its dependencies as 
intended. 

## Use the `autospec` parameter with patch: 

When using patch, consider setting the autospec=True parameter. This 
automatically creates a mock object that has the same methods and 
attributes as the original object, which can help catch issues related to 
incorrect method names or signatures. 

## Understand the difference between MagicMock and Mock: 

Use MagicMock when you need your mock object to support magic methods, and 
use the more lightweight Mock for other cases. This can help avoid 
unnecessary complexity in your tests. 

## Document your mocks: 

When creating complex mock objects or configurations, add comments to 
explain the purpose and behavior of each mock. This can help other 
developers understand and maintain your tests more easily.

By following these best practices and tips, you can create more effective 
and maintainable tests using the unittest.mock module. Remember that the 
primary goal of testing is to validate the correctness of your code, so 
always focus on writing tests that effectively cover your code's 
functionality and behavior.


## What are the strategies to avoid "over-mocking"?

Over-mocking can lead to brittle and less effective tests. Here are some 
strategies to avoid over-mocking in your tests: 

1. **Test behavior, not implementation**: Focus on testing the expected 
behavior and output of your code, rather than the internal implementation 
details. This allows your tests to remain relevant even when the 
implementation changes. You should only mock external dependencies or parts 
of the code that are not the primary focus of the test. 

2. **Use real objects when possible**: If it's feasible to use real objects 
in your tests without introducing complexity or dependencies, do so. This 
can provide more realistic testing conditions and help you catch issues 
that you might miss with mocks. 

3. **Leverage dependency injection**: Use dependency injection to pass 
dependencies to your functions or objects, making it easier to replace them 
with mock objects during testing. This can help reduce the need for mocking 
multiple objects and make your tests more focused. 

4. **Utilize integration tests**: In addition to unit tests, use 
integration tests to test how different components of your application work 
together. This can help you find issues that are not visible when testing 
components in isolation. 

5. **Apply the Test Pyramid principle**: Following the Test Pyramid 
principle, create a larger number of fast, focused unit tests, a smaller 
number of integration tests, and an even smaller number of end-to-end 
tests. This balance of test types can help ensure that your tests provide 
broad coverage while minimizing the need for mocking. 

6. **Keep mocks simple**: When creating mock objects, avoid adding 
unnecessary complexity. Define only the behavior necessary for the test, 
and avoid mocking every single method or attribute. 

7. **Isolate the code under test**: Structure your code in a modular way, 
so that each function or class has a single responsibility. This can help 
reduce the need for mocking multiple dependencies in a single test. 

8. **Be cautious when mocking built-ins**: Mocking built-in Python 
functions and objects can make your tests harder to understand and 
maintain. Use caution when mocking built-ins and consider alternative 
approaches, such as using real objects or wrapping built-ins in custom 
functions that can be more easily mocked. 

By applying these strategies, you can avoid over-mocking in your tests, 
which can help you create more robust and effective test suites. Remember 
that the goal of testing is to ensure the correctness and reliability of 
your code, so always focus on writing tests that achieve this objective 
without introducing unnecessary complexity. 

