# unittest - Mocking and Patching

Here are the key points about mocking and patching in the context of the `
unittest.mock` module: 

1. **Purpose of Mocking and Patching:** Mocking and patching allow you to 
replace parts of your code under test with mock objects. This is useful for 
isolating the code being tested from its dependencies, such as external 
services or complex subsystems. 

2. The `unittest.mock` Module: The `unittest.mock` module, introduced in 
Python 3.3 as part of the standard library, provides classes and functions 
for creating and working with mock objects. 

3. **Mock Objects:** A mock object is a dummy object that mimics the behavior 
of a real object or function. It allows you to control its behavior, return 
values, and simulate various scenarios for testing. 

4. **Patching:** Patching is the process of replacing an object or function 
with a mock object during the execution of a test. It is typically done using 
the `@unittest.mock.patch()` decorator or the `unittest.mock.patch` context 
manager. 

5. **Patch Decorator:** The `@unittest.mock.patch()` decorator is used to 
patch objects or functions at the location where the test method is defined. 
It automatically replaces the specified object or function with a mock object 
for the duration of the test. 

6. **Patch Context Manager:** The `unittest.mock.patch` context manager 
allows you to patch objects or functions within a specific block of code, 
typically within the test method. It provides more flexibility in patching 
multiple objects or patching in nested contexts. 

7. **Target Specification:** The target specification parameter of the patch 
decorator or context manager is used to specify the object or function to be 
patched. It can be specified as a string representing the import path or as a 
reference to the object or function itself. 

8. **Return Values and Side Effects:** You can specify return values and side 
effects for mock objects using the `return_value` and `side_effect` 
attributes. These allow you to control the behavior of the mock object during 
testing. 

9. **Assertion Methods:** The `unittest.mock` module provides a range of 
assertion methods to verify how mock objects are used during testing. These 
methods include `assert_called()`, `assert_called_with()`, `
assert_called_once()`, and more. 

10. **Call Arguments:** Mock objects keep track of the arguments with which 
they are called. You can access these arguments using the `call_args` or `
call_args_list` attributes of the mock object. 

11. **MagicMock:** The `MagicMock` class is a subclass of `Mock` that 
provides a set of default magic methods, allowing it to behave like any other 
Python object. It is particularly useful when mocking classes or instances. 

12. **Attribute Access:** Mock objects can simulate attribute access. You can 
specify return values or side effects for attributes using the `return_value` 
and `side_effect` attributes on the mock object. 

13. **Verifying Calls:** You can use methods like `call_count`, `called`, `
call_args`, and `call_args_list` to verify the number of times a mock object 
is called and the arguments with which it is called. 

14. **Patching Patch Objects:** You can patch a patch object itself to 
control when a patch takes effect or stops. This can be useful when you want 
to dynamically enable or disable patches based on certain conditions. 
