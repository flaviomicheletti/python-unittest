# unittest - Assertions

Here are the key points about assertions in the context of the `unittest` module:

1. **Purpose of Assertions:** Assertions are statements that verify the expected 
behavior of the code being tested. They help ensure that certain conditions 
are met during the execution of a test. 

2. **Using `assert` Statements:** In Python, you can use the `assert` keyword to 
define assertions. It takes a condition that should evaluate to `True`. If 
the condition is `False`, an `AssertionError` is raised. 

3. **Assertion Methods in `unittest.TestCase`:** The `unittest.TestCase` class 
provides a set of assertion methods that you can use within your test 
methods. These methods are more expressive and provide additional features 
compared to simple `assert` statements. 

4. **Common Assertion Methods:**
   - `assertEqual(a, b)`: Checks if `a` is equal to `b`.
   - `assertNotEqual(a, b)`: Checks if `a` is not equal to `b`.
   - `assertTrue(x)`: Checks if `x` is `True`.
   - `assertFalse(x)`: Checks if `x` is `False`.
   - `assertIs(a, b)`: Checks if `a` and `b` are the same object.
   - `assertIsNot(a, b)`: Checks if `a` and `b` are not the same object.
   - `assertIn(a, b)`: Checks if `a` is in `b`.
   - `assertNotIn(a, b)`: Checks if `a` is not in `b`.
   - `assertIsInstance(a, b)`: Checks if `a` is an instance of class `b`.
   - `assertNotIsInstance(a, b)`: Checks if `a` is not an instance of class `b`.

5. **Failure Messages:** Assertion methods provide an optional `msg` parameter 
where you can specify a custom failure message. This message helps in 
identifying the cause of the failure when an assertion fails. 

6. **Assertion Comparisons:** The assertion methods allow for different types of 
comparisons, such as numeric comparisons (`assertGreater()`, `assertLess()`), 
container membership (`assertCountEqual()`), and approximate floating-point 
equality (`assertAlmostEqual()`). 

7. **Custom Assertion Methods:** You can create your own custom assertion methods 
by defining new methods within your `unittest.TestCase` subclass. This can be 
useful for creating specialized assertions specific to your test cases. 

8. **Expected Failures:** Sometimes, you may expect a test to fail due to known 
issues or incomplete functionality. You can use the `
@unittest.expectedFailure` decorator to mark a test method as an expected 
failure. If the test fails as expected, it is not counted as a failure. 


## Assertions

In the `unittest` module in Python, there are several functions related to 
assertions that can be used for testing purposes. These functions are 
provided by the `TestCase` class, which is the base class for defining unit 
tests. Here are the commonly used assertion functions in `unittest`: 

1. `assertEqual(a, b)`: Asserts that `a` is equal to `b`.
2. `assertNotEqual(a, b)`: Asserts that `a` is not equal to `b`.
3. `assertTrue(x)`: Asserts that `x` is `True`.
4. `assertFalse(x)`: Asserts that `x` is `False`.
5. `assertIs(a, b)`: Asserts that `a` is identical to `b`.
6. `assertIsNot(a, b)`: Asserts that `a` is not identical to `b`.
7. `assertIsNone(x)`: Asserts that `x` is `None`.
8. `assertIsNotNone(x)`: Asserts that `x` is not `None`.
9. `assertIn(a, b)`: Asserts that `a` is a member of `b`.
10. `assertNotIn(a, b)`: Asserts that `a` is not a member of `b`.
11. `assertIsInstance(a, b)`: Asserts that `a` is an instance of `b`.
12. `assertNotIsInstance(a, b)`: Asserts that `a` is not an instance of `b`.
13. `assertAlmostEqual(a, b)`: Asserts that `a` is approximately equal to `b`.
14. `assertNotAlmostEqual(a, b)`: Asserts that `a` is not approximately equal to `b`.
15. `assertGreater(a, b)`: Asserts that `a` is greater than `b`.
16. `assertGreaterEqual(a, b)`: Asserts that `a` is greater than or equal to `b`.
17. `assertLess(a, b)`: Asserts that `a` is less than `b`.
18. `assertLessEqual(a, b)`: Asserts that `a` is less than or equal to `b`.
19. `assertRegex(s, r)`: Asserts that the regular expression `r` matches the string `s`.
20. `assertNotRegex(s, r)`: Asserts that the regular expression `r` does not match the string `s`.

These assertion functions can be used to validate different conditions in 
your unit tests and ensure that the expected behavior of your code is met. 

