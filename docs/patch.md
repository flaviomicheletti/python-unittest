# unittest.mock.patch

`unittest.mock.patch` is a powerful tool in the Python `unittest` module that 
allows you to temporarily modify the behavior of an object or function for 
the purpose of testing. Here are the most important concepts and techniques 
you need to understand to grasp the majority of `unittest.mock.patch` 
functionality: 

1. **Mocking:** `unittest.mock.patch` allows you to create mock objects, 
which are objects that simulate the behavior of real objects or functions. 

2. **Decorators:** `patch` can be used as a decorator to temporarily replace 
an object or function with a mock. 

3. **Context managers:** `patch` can also be used as a context manager to 
define a block of code within which an object or function is temporarily 
replaced with a mock. 

4. **Patch target:** The target of the patch can be specified as a string, 
representing the module path, or as an object or function. 

5. **Module-level patching:** When patching at the module level, the target 
is the module or package being imported, and `patch` will replace the target 
in all modules that import it. 

6. **Function-level patching:** When patching at the function level, the 
target is the specific function being used, and `patch` will only replace the 
target within that function. 

7. **Automatic cleanup:** `patch` automatically cleans up the patching after 
the test or the decorated code block finishes execution. 

8. **Returning values:** By default, mocks created by `patch` return another 
mock when called or accessed, but you can customize the return value using 
the `return_value` attribute. 

9. **Side effects:** You can define side effects for mocks, such as raising 
exceptions, by assigning a callable object to the `side_effect` attribute. 

10. **Assertions:** `unittest.mock.patch` provides various assertions to help 
you verify the usage of mocks, such as `assert_called`, `
assert_called_once`, `assert_called_with`, etc. 

11. **Attribute access:** Mocks created by `patch` can be used to mock both 
function calls and attribute access on objects. 

12. **Function call tracking:** Mocks keep track of how they are called, 
including the number of calls, the arguments passed, and more. 

13. **Nested patching:** You can use multiple `patch` decorators or context 
managers to patch multiple objects or functions simultaneously. 

14. **Specifying return values:** The `return_value` attribute of a mock can 
be set to a specific value or an iterable of values to be returned on each 
call. 

15. **Patch order:** The order in which you apply multiple patches can affect 
the behavior of your tests. The patches are applied from outermost to 
innermost. 

16. **Temporary attribute patching:** `patch` can be used to temporarily 
replace an attribute of an object with a mock. 

17. **Magic methods:** You can mock the behavior of magic methods, such as `
__enter__` and `__exit__`, using `patch`. 

18. **Property patching:** `patch` can be used to temporarily replace a 
property of an object with a mock. 

19. **Coroutine mocking:** `patch` can be used to mock coroutines and async 
functions. 

20. **Patch objects:** When using `patch` as a context manager, it returns a 
patch object that allows you to access information about the patch, such as 
the original target. 


