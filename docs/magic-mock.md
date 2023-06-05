# unittest.mock.MagicMock

`unittest.mock.MagicMock `is a powerful tool in Python's unittest.mock module 
that allows you to create mock objects and define their behavior during 
testing. Here are the key points that will help you understand the majority 
of its functionality: 

1. **Mock Objects:** MagicMock is a subclass of the Mock class and provides 
additional magic methods that enable you to define behavior and return values 
for attributes and method calls. 

2. **Method Calls:** MagicMock can be used to mock method calls by defining 
return values, side effects, or raising exceptions. 

3. **Return Values:** You can specify the return value of a mocked method by 
assigning a value to the method. For example, `mocked_obj.method.return_value = 42`. 

4. **Side Effects:** MagicMock allows you to define side effects for method calls 
using the `side_effect` attribute. You can assign a function or an iterable 
to execute custom logic when the mocked method is called. 

5. **Raising Exceptions:** You can configure a MagicMock to raise an exception 
when a specific method is called by assigning an exception object to the `
side_effect` attribute. 

6. **Attribute Access:** MagicMock can also be used to mock attribute access.
You can assign values directly to the attributes of a MagicMock object. 

7. **Method Existence:** MagicMock objects have a `method_calls` attribute that 
records the method calls made on the object. You can assert if a method was 
called using the `assert_called_with()` or `assert_called_once_with()` methods. 

8. **Assertions:** MagicMock provides several assertion methods such as `
assert_called_with()`, `assert_called_once_with()`, and `assert_called()`, 
which help verify that methods were called with specific arguments. 

9. **Call Counting:** You can assert the number of times a method was called 
using methods like `assert_called_once()` or `assert_called_once_with()`. 

10. **Resetting:** You can reset a MagicMock object's state by calling the `
reset_mock()` method. It clears the history of method calls and resets any 
configuration made on the object. 

11. **Property Mocking:** MagicMock can also be used to mock properties. You can 
assign values directly to property attributes, and they will be accessible as 
if they were real properties. 

12. **Chaining Mocks:** MagicMock objects can be chained together to create more 
complex mocks. This allows you to define different behaviors for different 
attributes and methods. 

13. **Async Mocking:** MagicMock supports async methods and can be used to mock 
async functions and coroutines. 

14. **Patching:** You can use MagicMock in conjunction with the `patch()` 
decorator or context manager to replace real objects or functions with mocks 
during testing. 

15. **Inspecting Calls:** MagicMock records every call made to the object, 
including the arguments and return values. You can access this information 
using the `call_args` and `call_args_list` attributes. 

16. **Flexible Matching:** MagicMock provides flexible matching options, such as 
using `call_args` to check if the arguments match a specific pattern or 
using `call_count` to verify the number of times a method was called. 

17. **Combining Matchers:** You can use matchers from the `unittest.mock` module, 
such as `Any`, `Instance`, or `Mock` instances, to create complex matching 
conditions for method arguments. 

18. **Asserting Unordered Calls:** You can assert that a method was called with 
specific arguments, irrespective of the order in which the calls occurred, 
using the `assert_has_calls()` method. 

19. **Configuring Iterables:** MagicMock can be configured to behave like an 
iterable, allowing you to specify the return values of successive calls using 
the `side_effect` attribute. 

20. **Patching Modules:** You can use MagicMock in combination with the `patch()` 
decorator or context manager to mock entire modules, replacing all functions 
and classes within the module with mock objects. 


