# unittest.mock.MagicMock - Return Values

Here are the key points that will help you understand the majority of how 
return values work in MagicMock:

1. **Return Value Assignment:** You can assign a specific return value to a 
mocked method using the dot notation. For example, `
mocked_obj.method.return_value = 42` sets the return value of the `method` 
to `42`. 

2. **Return Value on Method Call:** When the mocked method is called, it will 
return the assigned return value instead of executing the actual method 
logic. 

3. **Common Return Values:** You can assign any value to the return_value 
attribute, such as integers, strings, lists, or even other MagicMock objects. 

4. **Dynamic Return Values:** Return values can also be assigned dynamically by 
using callable objects or functions as the assigned value. For example, you 
can assign a lambda function that generates a unique value for each method 
call. 

5. **Return Value Types:** MagicMock allows you to assign different return values 
for different method calls. You can define a sequence of return values using 
lists, iterators, or even custom iterable objects. 

6. Side Effect vs. Return Value: While return values determine the value 
returned by a mocked method, side effects determine the behavior or action 
taken during method execution. They can be used together or separately to 
define the behavior of the mocked method. 

7. **Resetting Return Values:** You can reset the assigned return values of a 
MagicMock object by assigning a new value to the `return_value` attribute or 
by using the `reset_mock()` method to clear all configurations. 

8. **Exception Handling:** MagicMock allows you to assign an exception object to 
the `side_effect` attribute, which will cause the mocked method to raise the 
exception when called. This can be used to simulate error conditions during 
testing. 

9. **Side Effect Priority:** When both return values and side effects are defined 
for a mocked method, the side effect takes precedence. This means that if a 
side effect is defined, the return value will not be used. 

10. **Multiple Method Calls:** If you want a mocked method to return different 
values for each subsequent call, you can either assign an iterable as the 
return value or use the `side_effect` attribute to define a function or 
iterable that generates different return values. 

11. Call-specific Return Values: You can assign different return values based 
on specific method call arguments. This can be achieved by configuring the `
side_effect` attribute to a function that examines the arguments and returns 
a corresponding value. 

12. **Callable Return Values:** You can assign a callable object (such as a 
function or MagicMock) as the return value. This allows you to dynamically 
generate the return value based on the method call. 

13. **Call Count Impact:** Each time a method is called on a MagicMock object, 
the return value will be determined by the next item in the assigned return 
value sequence. If there are no more items, it will return the last assigned 
return value. 

14. **Asserting Return Values:** You can assert that a method was called with 
specific arguments and returned the expected value using the `
assert_called_with()` and `assert_called_once_with()` assertion methods 
provided by MagicMock. 

15. **Default Return Value:** If you haven't explicitly assigned a return value 
for a mocked method, it will return a new MagicMock object by default. This 
allows you to chain method calls and define behavior for attributes and 
nested methods. 


