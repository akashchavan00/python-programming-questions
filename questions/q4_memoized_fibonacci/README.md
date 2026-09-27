# Q4: Memoized Recursion with a Custom Decorator

## Question
1. Write a plain recursive function `fib(n)` that computes the n-th Fibonacci number.
2. Write your own `@memoize` decorator (do **not** use `functools.lru_cache`) that caches results of any function based on its arguments.
3. Apply `@memoize` to a second Fibonacci function `fib_memo(n)` and compare the execution time of `fib(30)` vs `fib_memo(30)` to show the performance difference.
4. Also apply your `@memoize` decorator to a recursive `factorial(n)` function to prove it's reusable for any function, not just Fibonacci.

## Approach
1. A decorator is just a function that takes a function and returns a wrapped version of it — this relies on functions being first-class objects in Python.
2. Inside `memoize`, keep a `cache` dictionary in the enclosing scope (a **closure**) that persists across calls because it's defined outside the inner `wrapper` function but the `wrapper` still holds a reference to it.
3. The wrapper builds a hashable key from `*args`/`**kwargs`, checks whether that key is already in the cache; if so it returns the cached result instead of recomputing, otherwise it calls the original function, stores the result, and returns it.
4. `functools.wraps` is used to preserve the original function's `__name__` and docstring (good practice, not strictly required for correctness).
5. The `time` module is used to benchmark both versions and print the speed-up factor.

## Concepts Used
- Recursion and recursive problem decomposition
- Decorators and higher-order functions
- Closures (the `cache` dict captured by `wrapper`)
- `*args, **kwargs` for generic function wrapping
- `functools.wraps`
- Dictionaries used as a cache / memoization table
- Basic performance benchmarking with the `time` module
