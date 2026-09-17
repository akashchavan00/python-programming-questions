"""
Q6: Generators & Lazy Infinite Sequences
Demonstrates yield, the iterator protocol, and itertools.islice
with infinite prime and Fibonacci generators.
"""

import math
from itertools import islice


def primes():
    """Infinite generator of prime numbers, computed lazily."""
    found = []
    candidate = 2
    while True:
        limit = math.isqrt(candidate)
        is_prime = all(candidate % p != 0 for p in found if p <= limit)
        if is_prime:
            found.append(candidate)
            yield candidate
        candidate += 1


def fibonacci():
    """Infinite generator of Fibonacci numbers, computed lazily."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def nth_prime(n):
    """Return the n-th prime (1-indexed) without precomputing more than needed."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return next(islice(primes(), n - 1, n))


def main():
    print("First 10 primes:", list(islice(primes(), 10)))
    print("First 10 Fibonacci numbers:", list(islice(fibonacci(), 10)))

    for n in (1, 5, 20):
        print(f"The {n}-th prime is {nth_prime(n)}")

    # Demonstrate laziness: manually pull values with next()
    prime_gen = primes()
    print("\nPulling primes one at a time with next():")
    for _ in range(5):
        print(" ", next(prime_gen))


if __name__ == "__main__":
    main()
