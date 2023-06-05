# unittest.mock.Mock - Method Calls

Here are the most important points regarding method calls with `
unittest.mock.Mock`: 

1. **Simulating Method Calls:** `unittest.mock.Mock` allows you to simulate 
method calls on a mock object and define the behavior of those calls during 
testing. 

2. **Setting Return Values:** You can use the dot notation to define the 
return value of a specific method call on a mock object. For example, `
my_mock.method.return_value = 10` will make `my_mock.method()` return `10` 
when called. 

3. **Asserting Method Calls:** `unittest.mock.Mock` provides various 
assertion methods to verify that specific methods were called with certain 
arguments or in a particular order. For example, you can use `
assert_called_with()` to check if a method was called with specific 
arguments. 

4. **Call Counting:** Mock objects keep track of how many times methods are 
called. You can access the call count using the `call_count` attribute. For 
example, `my_mock.method.call_count` will give you the number of times `
my_mock.method()` was called. 

5. **Return Value per Call:** You can specify different return values for 
consecutive calls to the same method using the `side_effect` attribute. This 
allows you to create more complex behavior where the return value depends on 
the specific call. 

6. **`call_args` and `call_args_list`:** Mock objects store information about 
the arguments passed to each method call. The `call_args` attribute provides 
the arguments of the most recent call, while `call_args_list` contains all 
the call arguments in the order they were made. 

7. **Method Chaining:** Mock objects support method chaining, allowing you to 
call multiple methods on a mock object in a single line of code. For 
example, `my_mock.method1().method2().method3()` is a valid chain of method 
calls on `my_mock`. 

8. **Attribute Access on Methods:** You can also simulate attribute access on 
methods of a mock object. For example, you can set attributes on `
my_mock.method` using dot notation (`my_mock.method.attribute = 'value'`) and 
access them (`my_mock.method.attribute`) during testing. 

9. **Combining Return Values and Method Calls:** You can use both the `
return_value` attribute and method calls together. If the `return_value` is 
defined, it will be returned when the method is called, but you can still 
assert that the method was called with specific arguments. 

10. **Handling Unexpected Method Calls:** By default, `unittest.mock.Mock` 
allows any method to be called without raising an error. You can use the `
spec` or `spec_set` attributes to restrict the mock to only accept specific 
methods, raising an attribute error if an unexpected method is called. 

Understanding these key concepts will give you a solid foundation for working 
with method calls in `unittest.mock.Mock`. You'll be able to simulate method 
behavior, set return values, assert method calls, and track call counts 
during your tests. 


