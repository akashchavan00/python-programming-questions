# Q6: Generators & Lazy Infinite Sequences

## Question
1. Write a generator function `primes()` that lazily yields prime numbers forever (2, 3, 5, 7, 11, ...) without precomputing a fixed range.
2. Write a generator function `fibonacci()` that lazily yields the Fibonacci sequence forever.
3. Using `itertools.islice`, get the first 10 primes and the first 10 Fibonacci numbers without ever materializing an infinite list.
4. Write a function `nth_prime(n)` that returns just the n-th prime using your generator (demonstrating that generators only compute as much as needed).

## Approach
1. A generator function uses `yield` instead of `return`; each call to `next()` resumes execution right after the last `yield`, which is what makes infinite sequences possible without infinite memory.
2. For `primes()`, keep a growing list of found primes and test each new candidate by trial division against only the primes found so far, up to its integer square root (a standard optimization — no need to test factors bigger than `sqrt(candidate)`).
3. For `fibonacci()`, keep two running values `a, b` and `yield a`, then update `a, b = b, a + b` inside an infinite `while True` loop.
4. `itertools.islice(generator, n)` lazily pulls a finite number of values from an infinite generator — it's the generator equivalent of list slicing, without ever asking the generator to finish (which it never would).
5. `nth_prime(n)` shows how generators let you compute "just enough" rather than a whole list up front, which is more memory-efficient than, say, building a list of the first 1000 primes just to look at the 5th one.

## Concepts Used
- Generators and the `yield` keyword
- The iterator protocol (`__iter__`, `__next__`, lazy evaluation)
- Infinite sequences without infinite memory
- `itertools.islice` for lazily limiting an iterator
- Algorithmic thinking (primality testing, trial division up to sqrt)
- `math.isqrt` for integer square roots
