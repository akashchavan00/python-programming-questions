# 10 Medium-Level Python Practice Questions

Each folder contains:
- `README.md` — the question, the approach to solving it, and the concepts it uses.
- `solution.py` — a runnable, commented solution with a `main()` demo you can execute directly.

Run any solution with:
```
python3 solution.py
```

## Question Index

| # | Folder | Topic | Key Concepts |
|---|--------|-------|---------------|
| 1 | q1_word_frequency_counter | Word Frequency Counter | regex, `collections.Counter`, custom sort keys |
| 2 | q2_balanced_brackets | Balanced Brackets Validator | stacks, dictionaries, string parsing |
| 3 | q3_library_management_system | Library Management System | OOP, inheritance, polymorphism, encapsulation |
| 4 | q4_memoized_fibonacci | Memoized Recursion with Custom Decorator | decorators, closures, recursion, benchmarking |
| 5 | q5_context_managers | Custom Context Managers | `with` statement, `__enter__`/`__exit__`, `contextlib` |
| 6 | q6_prime_generator | Generators & Lazy Infinite Sequences | `yield`, iterators, `itertools.islice` |
| 7 | q7_bank_account_system | Bank Account with Custom Exceptions | custom exceptions, `try/except/else/finally` |
| 8 | q8_anagram_palindrome | Anagram Grouping & Palindrome Checker | `defaultdict`, hashing, two-pointer technique |
| 9 | q9_lru_cache | LRU Cache from Scratch | `collections.OrderedDict`, cache design, O(1) ops |
| 10 | q10_json_contact_book | JSON Contact Book (CRUD) | file I/O, `json` module, `**kwargs` |

Together these 10 questions touch: OOP (classes, inheritance, polymorphism, encapsulation, dunder methods), decorators & closures, generators & the iterator protocol, recursion & memoization, custom exceptions & full exception-handling flow, context managers, regular expressions, the `collections` module (`Counter`, `defaultdict`, `OrderedDict`), stacks, hashing, the two-pointer technique, JSON & file persistence, and writing clean, testable functions.

Suggested order: solve them 1 → 10, since later ones assume comfort with basics like functions, dicts, and classes covered in the earlier ones — but each is self-contained, so feel free to jump around based on which concept you want to practice.
