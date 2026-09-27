"""
Q4: Memoized Recursion with a Custom Decorator
Implements a hand-rolled @memoize decorator and applies it to
Fibonacci and factorial to demonstrate the speedup over plain recursion.
"""

import time
import functools


def memoize(func):
    """
    A decorator that caches a function's return value based on its arguments.
    Uses a closure: `cache` lives in the enclosing scope of `wrapper`
    and persists between calls because `wrapper` keeps a reference to it.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # kwargs.items() must be sorted/frozen to build a consistent, hashable key.
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache  # exposed for inspection/testing
    return wrapper


def fib(n):
    """Plain recursive Fibonacci - exponential time complexity."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@memoize
def fib_memo(n):
    """Memoized recursive Fibonacci - linear time complexity after caching."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


@memoize
def factorial(n):
    """Memoized recursive factorial - shows @memoize works for any function."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def timed(label, func, *args):
    start = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - start
    print(f"{label}: result={result}, time={elapsed:.6f}s")
    return elapsed


def main():
    n = 30

    slow_time = timed(f"fib({n})       (no memo)", fib, n)
    fast_time = timed(f"fib_memo({n})  (memoized)", fib_memo, n)

    if fast_time > 0:
        print(f"\nSpeed-up: ~{slow_time / fast_time:,.0f}x faster with memoization")

    print(f"\nfactorial(10) = {factorial(10)}")
    print(f"Cache entries for factorial: {len(factorial.cache)}")


if __name__ == "__main__":
    main()
