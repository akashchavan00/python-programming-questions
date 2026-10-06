# Python match Statement

The `match` statement (**structural pattern matching**) was added in **Python 3.10**. It compares a value against a series of patterns and runs the block of the first pattern that matches. It is similar to `switch` in other languages, but much more powerful: it can match shapes of data (lists, dicts, objects), not just equal values.

> Requires Python 3.10 or newer. Check with `python --version`.

## Contents

1. [Basic syntax](#1-basic-syntax)
2. [Default case (wildcard `_`)](#2-default-case-wildcard-_)
3. [Combining patterns with `|` (OR)](#3-combining-patterns-with--or)
4. [Guards (`if` in a case)](#4-guards-if-in-a-case)
5. [Capture patterns](#5-capture-patterns)
6. [Matching sequences (lists / tuples)](#6-matching-sequences-lists--tuples)
7. [Matching dictionaries (mappings)](#7-matching-dictionaries-mappings)
8. [Matching class instances](#8-matching-class-instances)
9. [The `as` keyword](#9-the-as-keyword)
10. [Value patterns (dotted names, Enum)](#10-value-patterns-dotted-names-enum)
11. [Literal patterns (`None`, `True`, `False`)](#11-literal-patterns-none-true-false)
12. [Nested patterns](#12-nested-patterns)
13. [match vs if-elif](#13-match-vs-if-elif)
14. [Common mistakes](#14-common-mistakes)
15. [Quick summary](#15-quick-summary)

---

## 1. Basic syntax

```python
match subject:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default
```

```python
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")     # runs
    case 5:
        print("Friday")
```

**How it works**
- The subject expression is evaluated **once**.
- Cases are tested **top to bottom**.
- The **first** matching case runs, then the whole `match` ends. There is **no fall-through** and **no `break` needed**.
- If nothing matches and there is no default case, nothing happens (no error).

---

## 2. Default case (wildcard `_`)

`_` is the **wildcard** pattern. It matches anything and does not bind a variable. Use it as the last case, like `default` in `switch`.

```python
day = 8

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Not a valid weekday")   # runs
```

The wildcard (or any capture pattern) must be **last**. Putting it earlier causes a `SyntaxError` ("wildcard makes remaining patterns unreachable").

---

## 3. Combining patterns with `|` (OR)

Use `|` to match several values in one case.

```python
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")      # runs
    case _:
        print("Invalid day")
```

```python
command = "quit"

match command:
    case "q" | "quit" | "exit":
        print("Bye!")         # runs
    case _:
        print("Unknown command")
```

---

## 4. Guards (`if` in a case)

A **guard** adds an extra condition to a case. The case matches only if the pattern matches **and** the guard is True.

```python
month = 5
day = 15

match day:
    case 1 | 2 | 3 if month == 5:
        print("Early May")
    case d if d > 10 and month == 5:
        print("Late May")     # runs
    case _:
        print("Other")
```
d is a capture pattern.
```python
n = -7

match n:
    case 0:
        print("zero")
    case x if x > 0:
        print("positive")
    case x if x < 0:
        print("negative")     # runs
```

---

## 5. Capture patterns

A bare name in a pattern **captures** the value into that variable.

```python
point = 42

match point:
    case 0:
        print("zero")
    case value:
        print(f"captured {value}")   # captured 42
```

Important: a bare name **always matches** and **binds**. It does **not** compare against an existing variable.

```python
RED = "red"
color = "blue"

match color:
    case RED:                 # NOT a comparison! Captures "blue" into RED
        print("matched")      # runs (surprising!)
```

To compare against a constant, use a **dotted name** (see [Value patterns](#10-value-patterns-dotted-names-enum)).

---

## 6. Matching sequences (lists / tuples)

Patterns can describe the **shape** of a list or tuple and unpack it at the same time.

```python
match [1, 2]:
    case []:
        print("empty")
    case [x]:
        print("one item", x)
    case [x, y]:
        print("two items", x, y)         # runs
    case [x, y, z]:
        print("three items")
```

**Star pattern (`*`)** captures the rest of the items into a list:

```python
match [1, 2, 3, 4, 5]:
    case [first, *rest]:
        print(first, rest)               # 1 [2, 3, 4, 5]
```

```python
match ["move", 10, 20]:
    case ["move", x, y]:
        print(f"Moving to {x},{y}")      # runs
    case ["stop"]:
        print("Stopping")
```

```python
match [1, 2, 3, 4]:
    case [first, *middle, last]:
        print(first, middle, last)       # 1 [2, 3] 4
```

**Key points**
- Works on `list`, `tuple` and other sequences.
- Does **not** match `str`, `bytes` or `bytearray` as sequences (a string is matched as a whole value).
- Only **one** star pattern is allowed per sequence pattern.
- Use `*_` to ignore the remaining items.

```python
command = "go north"
match command.split():
    case ["go", direction]:
        print("Going", direction)        # Going north
    case ["pick", "up", item]:
        print("Picked", item)
    case _:
        print("Unknown")
```

---

## 7. Matching dictionaries (mappings)

Mapping patterns match dictionaries by **keys**. Only the listed keys must exist; extra keys are **ignored**.

```python
user = {"name": "Akash", "role": "admin", "age": 25}

match user:
    case {"role": "admin", "name": name}:
        print(f"Admin: {name}")          # Admin: Akash
    case {"role": "guest"}:
        print("Guest")
```

Capture the remaining items with `**rest`:

```python
match {"a": 1, "b": 2, "c": 3}:
    case {"a": 1, **rest}:
        print(rest)                      # {'b': 2, 'c': 3}
```

**Key points**
- Keys must be literals or dotted names (not variables).
- `{}` matches **any** mapping (it does not require an empty dict).

---

## 8. Matching class instances

Class patterns check the type **and** pull out attributes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(0, 5)

match p:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"On the Y axis at {y}")   # On the Y axis at 5
    case Point(x=x, y=0):
        print(f"On the X axis at {x}")
    case Point():
        print("Somewhere else")
```

**Positional patterns with `__match_args__`**

Dataclasses create `__match_args__` automatically, so positional patterns work:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

match Point(0, 3):
    case Point(0, 0):
        print("Origin")
    case Point(0, y):
        print(f"Y axis, y={y}")          # Y axis, y=3
```

For a normal class, define it yourself:

```python
class Point:
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y
```

**Built-in types** can be checked too:

```python
value = 3.14

match value:
    case int():
        print("integer")
    case float():
        print("float")                   # runs
    case str():
        print("string")
    case list() | tuple():
        print("list or tuple")
```

---

## 9. The `as` keyword

`as` captures the **whole** value matched by a sub-pattern.

```python
match 7:
    case 1 | 2 | 3 as small:
        print("small", small)
    case 4 | 5 | 6 | 7 as big:
        print("big", big)                # big 7
```

```python
match ["move", (3, 4)]:
    case ["move", (x, y) as coords]:
        print(x, y, coords)              # 3 4 (3, 4)
```

---

## 10. Value patterns (dotted names, Enum)

To compare against a **constant**, use a **dotted name** (`something.attribute`). Dotted names are looked up and compared with `==`, not captured.

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

color = Color.GREEN

match color:
    case Color.RED:
        print("Stop")
    case Color.GREEN:
        print("Go")                      # runs
    case Color.BLUE:
        print("Calm")
```

Using a class or module as a namespace for constants also works:

```python
class Status:
    OK = 200
    NOT_FOUND = 404

code = 404

match code:
    case Status.OK:
        print("Success")
    case Status.NOT_FOUND:
        print("Not found")               # runs
```

---

## 11. Literal patterns (`None`, `True`, `False`)

Literals (numbers, strings, `None`, `True`, `False`) are matched by value. `None`, `True` and `False` are compared with **identity** (`is`).

```python
value = None

match value:
    case None:
        print("Nothing")                 # runs
    case True:
        print("Yes")
    case False:
        print("No")
```

Note: `case True` will **not** match `1`, because `True` is matched with `is`.

---

## 12. Nested patterns

Patterns can be combined and nested to any depth.

```python
order = {
    "customer": {"name": "Ravi", "vip": True},
    "items": ["pen", "book"],
}

match order:
    case {"customer": {"name": name, "vip": True}, "items": [first, *_]}:
        print(f"VIP {name}, first item: {first}")   # VIP Ravi, first item: pen
```

```python
shapes = [("circle", 5), ("rect", 3, 4), ("square", 2)]

for shape in shapes:
    match shape:
        case ("circle", r):
            print("Circle area:", 3.14 * r * r)
        case ("rect", w, h):
            print("Rectangle area:", w * h)
        case ("square", s):
            print("Square area:", s * s)
```

---

## 13. match vs if-elif

| Feature | `if / elif` | `match` |
|---------|-------------|---------|
| Compare a value | Yes | Yes |
| Check shape of list/dict | Manual (`len()`, indexing) | Built in |
| Unpack values while testing | No | Yes |
| Check type and attributes | `isinstance()` + manual | Class patterns |
| Fall-through / `break` | N/A | Not needed |
| Python version | All | 3.10+ |

Same logic, two styles:

```python
# if / elif
if status == 200:
    msg = "OK"
elif status == 404:
    msg = "Not Found"
else:
    msg = "Unknown"

# match
match status:
    case 200:
        msg = "OK"
    case 404:
        msg = "Not Found"
    case _:
        msg = "Unknown"
```

Use `match` when you branch on the **structure** of data or have many discrete values. Use `if` for simple boolean conditions or ranges.

---

## 14. Common mistakes

1. **Using a variable as a constant**: `case RED:` captures instead of comparing. Use a dotted name (`Color.RED`) or a literal.
2. **Wildcard not last**: `case _:` (or a bare name) before other cases gives a `SyntaxError`.
3. **Expecting `break`**: not needed; only one case runs.
4. **Python < 3.10**: `match` is a `SyntaxError` on older versions.
5. **Matching strings as sequences**: `case [a, b]` will not match `"hi"`; split it first.
6. **Mixing alternatives with different captures**: with `|`, every alternative must bind the same names.
7. **Expecting an exact dict match**: mapping patterns ignore extra keys.

> `match` and `case` are **soft keywords**: they are only special in this context, so variables named `match` (e.g. from `re.match`) still work.

---

## 15. Quick summary

| Pattern | Example | Meaning |
|---------|---------|---------|
| Literal | `case 404:` | Equals the value |
| Wildcard | `case _:` | Matches anything (default) |
| Capture | `case x:` | Matches anything and binds to `x` |
| OR | `case 1 \| 2:` | Any of the alternatives |
| Guard | `case x if x > 0:` | Pattern plus extra condition |
| Sequence | `case [a, b]:` | List/tuple of that shape |
| Star | `case [a, *rest]:` | Capture remaining items |
| Mapping | `case {"k": v}:` | Dict containing key `k` |
| Class | `case Point(x=0):` | Instance of class with attributes |
| Value | `case Color.RED:` | Compare to a dotted name |
| As | `case 1 \| 2 as n:` | Bind the matched sub-pattern |
