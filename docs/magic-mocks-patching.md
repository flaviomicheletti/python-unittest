# unittest.mock.MagicMock - Patching

Here are the key points that will help you understand the majority of how 
patching works in MagicMock: 

1. **Purpose of Patching:** Patching allows you to replace real objects, 
functions, or modules with mock objects during testing. This is useful when 
you want to control the behavior or state of certain components in your code. 

2. **Decorator and Context Manager:** MagicMock provides two ways to apply 
patching: as a decorator (`@patch`) or as a context manager (`with patch`). 
Both approaches achieve the same result, and you can choose the one that fits 
your testing needs. 

3. **Target Objects:** When using patching, you specify the target object that 
you want to replace with a mock object. This can be a module, a class, a 
function, or an attribute. 

4. **Patching Modules:** You can patch entire modules by specifying the module's 
import path as the target object. This allows you to replace all functions 
and classes within the module with mock objects. 

5. **Patching Classes and Attributes:** If you want to patch a specific class or 
attribute within a module, you specify the complete import path of the class 
or attribute as the target object. 

6. **Automatic Cleanup:** MagicMock automatically cleans up the patches after the 
test has run, restoring the original objects or functions to their initial 
state. You don't need to manually revert the patching. 

7. **Patching Syntax:** When using patching as a decorator, you apply it directly 
above the test function you want to patch. When using it as a context 
manager, you wrap the code block that requires patching. 

8. **Mock Creation:** MagicMock automatically creates a mock object for the 
patched target. You can then configure the behavior and assertions of the 
mock object as needed. 

9. **Accessing Mocks:** If you need to access the created mock object for further 
configuration or assertions, you can use the `mock.patch()` function as a 
context manager and assign the mock object to a variable. 

10. **Configuring Behavior:** Once you have access to the mock object, you can 
configure its behavior using attributes like `return_value`, `side_effect`, 
or `async_side_effect`. This allows you to control the return values, 
exceptions, or side effects of the patched object. 

11. **Controlling Attributes:** MagicMock allows you to mock and control the 
behavior of attributes within patched objects. You can assign values to 
attributes or define behaviors for attribute access or assignment. 

12. **Assertion Methods:** You can use assertion methods provided by MagicMock, 
such as `assert_called_with()` or `assert_called_once_with()`, to verify that 
specific methods or attributes were called with the expected arguments during 
testing. 

13. **Multiple Patching:** You can apply multiple patches simultaneously by 
specifying multiple target objects and their corresponding mock objects as 
arguments to the patch decorator or context manager. 

14. **Patching Order:** When applying multiple patches, the order of the patches 
matters. Patching occurs from the outermost patch to the innermost patch, 
allowing you to control the behavior of nested components. 

15. **Patching Nesting:** You can nest patches to mock components within patched 
objects. The outer patches will mock the objects, and the inner patches will 
mock the nested components. 
