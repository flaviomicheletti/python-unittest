# unittest.mock.MagicMock - Async Mocking

Here are the key points that will help you understand the majority of how 
async mocking works in MagicMock: 

1. **Async Support:** MagicMock provides support for mocking async functions and 
coroutines, allowing you to simulate and control their behavior during 
testing. 

2. **Mocking Async Functions:** To mock an async function, create a MagicMock 
object and assign it to the function you want to mock. You can then define 
the behavior using attributes like `return_value`, `side_effect`, or `
async_side_effect`. 

3. **Mocking Async Coroutines:** To mock an async coroutine, create a MagicMock 
object and assign it to the coroutine. Similar to async functions, you can 
define the behavior using attributes like `return_value`, `side_effect`, or `
async_side_effect`. 

4. `await_` Prefix: When mocking an async function or coroutine, you can 
access the return value or define behavior using the `await_` prefix. For 
example, `mocked_coroutine.await_return_value = 42` sets the return value of 
the coroutine to `42`. 

5. **Coroutine Behavior:** MagicMock provides similar capabilities for async 
coroutines as regular methods. You can define return values, side effects, or 
raise exceptions using the assigned attributes. 

6. **Coroutine Side Effects:** Async coroutines in MagicMock can have side 
effects defined using the `async_side_effect` attribute. This allows you to 
execute custom logic or raise exceptions during coroutine execution. 

7. `await` Keyword: During testing, when you `await` the mocked async 
function or coroutine, it will return the assigned return value or raise the 
defined exception. This allows you to control the behavior of async code in a 
controlled testing environment. 

8. **Async Call Counting:** Similar to regular methods, you can use call counting 
methods and attributes such as `assert_called()`, `assert_called_once()`, `
assert_called_with()`, `assert_called_once_with()`, and `
assert_called_with_any()` to verify the number of times an async function or 
coroutine is awaited. 

9. **Patching Async Functions and Coroutines:** You can use MagicMock in 
conjunction with the `patch()` decorator or context manager to replace real 
async functions or coroutines with mock objects. This allows you to control 
the behavior of async code within specific test cases or test suites. 

10. **Coroutine Mocking Considerations:** When mocking async coroutines, it's 
important to ensure that the event loop is properly handled. You may need to 
patch or configure the event loop to ensure proper execution and testing of 
async code. 

11. **Asynchronous Libraries:** MagicMock's async mocking capabilities can be 
particularly useful when testing code that interacts with asynchronous 
libraries such as asyncio, aiohttp, or aioredis. 

12. **Async Assertion Helpers:** The `asyncio` module provides assertion helpers, 
such as `asyncio.assert_awaited()`, `asyncio.assert_awaited_with()`, and `
asyncio.assert_awaited_once_with()`, which can be used to assert the awaited 
calls on mocked async functions or coroutines. 

13. **Resetting Async Mocks:** You can reset the state of async mocks by calling 
the `reset_mock()` method, which clears the call history and resets any 
configured behavior. 


