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

