# unittest.mock.MagicMock - Call Counting

Here are the key points that will help you understand the majority of how 
call counting works in MagicMock:

1. **Call Counting Methods:** MagicMock provides several methods to assert the 
number of times a method is called. The most commonly used methods are `
assert_called()`, `assert_called_once()`, `assert_called_with()`, `
assert_called_once_with()`, and `assert_called_with_any()`. 

2. `assert_called()`: This method verifies that the mocked method was called 
at least once. It does not consider the specific arguments passed to the 
method. 

3. `assert_called_once()`: This method checks if the method was called 
exactly once. If the method is called multiple times, it raises an assertion 
error. 

4. `assert_called_with()`: This method verifies that the method was called at 
least once with specific arguments. It compares the arguments passed to the 
mocked method with the expected arguments. 

5. `assert_called_once_with()`: This method combines the functionality of `
assert_called_once()` and `assert_called_with()`. It checks if the method was 
called exactly once with the expected arguments. 

6. `assert_called_with_any()`: This method checks if the method was called at 
least once with any arguments. It does not specify any specific arguments to 
match against. 

7. **Call Count Attributes:** MagicMock provides several attributes that give you 
information about the number of times a method is called. The most commonly 
used attributes are `call_count`, `call_args`, and `call_args_list`. 

8. `call_count`: This attribute returns the total number of times the method 
was called. You can compare this count to expected values or use it in 
assertions. 

9. `call_args`: This attribute provides the arguments passed to the method 
during the most recent call. It returns `None` if the method was not called 
yet. 

10. `call_args_list`: This attribute contains a list of tuples, where each 
tuple represents the arguments passed to the method during a specific call. 
The most recent call's arguments are at the end of the list. 

11. **Resetting Call Counts:** You can reset the call count and clear the call 
history by using the `reset_mock()` method on the MagicMock object. 

12. **Combining Call Counts:** If you want to assert that a method was called a 
specific number of times, you can combine call counting methods and 
attributes. For example, you can use `assert_called_once()` to verify it was 
called once and then check the `call_count` attribute to ensure it wasn't 
called more times. 

13. **Verifying Order of Calls:** MagicMock also provides methods like `
assert_has_calls()` and `assert_called_once_with()` to verify the order of 
method calls and the arguments passed to them. 

14. **Negating Call Counts:** You can use the `assert_not_called()` method to 
assert that a method was not called at all. This is useful when you want to 
verify that a specific method should not be invoked during the test. 

15. **Chained Method Calls:** If a method is called multiple times in a chain, 
each call counts as a separate call. You can use `assert_has_calls()` to 
verify the sequence of calls. 


