# unittest.mock.Mock - Specifying Side Effects

Here are the most important points regarding specifying side effects with `
unittest.mock.Mock`: 

1. **Side Effect Basics:** A side effect in `unittest.mock.Mock` refers to an 
action that occurs when the mock object is called, instead of returning a 
specific value. This can be useful for simulating exceptions, raising errors, 
or performing custom actions during testing. 

2. **Using `side_effect` Attribute:** The `side_effect` attribute of a `Mock` 
object allows you to define a callable that will be executed when the mock is 
called. This callable can be a function, a lambda expression, or a reference 
to an existing function or method. 

3. **Callable as Side Effect:** When assigning a callable as the `
side_effect`, it will be invoked every time the mock is called. The callable 
will receive the same arguments as the mock and can perform any desired 
action, such as modifying variables, logging, or raising exceptions. 

4. **Returning Multiple Values:** The side effect callable can be used to 
return different values on subsequent calls. For example, you can use a list 
or an iterator and return different elements from it each time the mock is 
called. 

5. **Raising Exceptions:** The side effect callable can raise exceptions to 
simulate error scenarios. For instance, you can raise a specific exception 
like `ValueError` or create a custom exception and raise it during the side 
effect. 

6. **Dynamically Generating Return Values:** The side effect callable can 
calculate and return values based on the arguments passed to the mock. This 
is particularly useful when the desired return value depends on the specific 
inputs provided during the test. 

7. **Side Effect for Attribute Access:** The `side_effect` attribute can also 
be used to define the behavior when an attribute of the mock is accessed. You 
can assign a callable that will be executed when an attribute is accessed, 
allowing you to return dynamic values or raise exceptions. 

8. **Chaining Side Effects:** It's possible to chain multiple side effects by 
using the `side_effect` attribute multiple times or by defining a single 
callable that handles different scenarios based on conditional logic within 
the function. 

9. **Combining Return Values and Side Effects:** You can use both the `
return_value` attribute and the `side_effect` attribute together. If the `
side_effect` is defined, it takes precedence over the `return_value`, and the 
side effect will be executed instead of returning the value. 

10. **Error Handling in Side Effects:** When using side effects that raise 
exceptions, make sure to handle those exceptions appropriately in your tests. 
Use `try-except` blocks or assertions to verify that the expected exceptions 
are raised during the side effect. 

Understanding these key concepts will give you a solid foundation for working 
with side effects in `unittest.mock.Mock`. You'll be able to simulate complex 
behaviors, dynamically generate return values, and handle exceptions during 
testing. 


