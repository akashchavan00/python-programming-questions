# Q5: Custom Context Managers

## Question
1. Implement a **class-based** context manager `Timer` (using `__enter__` and `__exit__`) that measures and prints how long the code inside a `with` block took to run.
2. Implement a **function-based** context manager `safe_file_writer(path)` using `contextlib.contextmanager` and the `yield` keyword, which:
   - Opens a file for writing.
   - Yields the file handle to the `with` block.
   - Guarantees the file is closed even if an exception occurs inside the block.
   - Prints a message if an exception was raised, and suppresses it after logging (so the program can continue).

## Approach
1. For the class-based manager, `__enter__` records the start time and returns `self` (so callers can do `with Timer() as t: ...` and read `t.elapsed` afterward); `__exit__` computes the elapsed time and prints it. `__exit__` receives `(exc_type, exc_value, traceback)`, which lets it detect whether an exception happened inside the block.
2. For the function-based manager, everything before `yield` is the "setup" (like `__enter__`), and everything after `yield` — wrapped in `try/except/finally` — is the "teardown" (like `__exit__`). Catching the exception around the `yield` lets us log it, and *not* re-raising it means it's suppressed so execution continues after the `with` block.
3. Returning `True` from a class-based `__exit__` (or simply catching without re-raising in the generator version) suppresses the exception; returning `False`/`None` lets it propagate.
4. The demo deliberately raises an exception inside one `with safe_file_writer(...)` block to prove the file still gets closed and the program keeps running.

## Concepts Used
- The `with` statement / context manager protocol (`__enter__`, `__exit__`)
- `contextlib.contextmanager` decorator and generator-based context managers
- Exception handling inside context managers (`try/except/finally`)
- Resource management (files) and guaranteed cleanup
- The `time` module for measuring elapsed time
