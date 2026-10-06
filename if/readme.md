## Contents

1. [Python if](#1-python-if)
2. [Python elif](#2-python-elif)
3. [Python else](#3-python-else)
4. [Shorthand if](#4-shorthand-if)
5. [Shorthand if else (ternary)](#5-shorthand-if-else-ternary)
6. [Logical operators](#6-logical-operators)
7. [Nested if](#7-nested-if)
8. [pass statement](#8-pass-statement)

---

## 1. Python if

The `if` statement runs a block of code **only when its condition is `True`**.

```python
if condition:
    # code that runs when condition is True
```

```python
a = 33
b = 200
if b > a:
    print("b is greater than a")   # runs
```

**Key points**
- The condition ends with a colon `:`.
- **Indentation** (usually 4 spaces) defines the block. Python has no braces `{}`; missing or inconsistent indentation raises `IndentationError`.
- Any expression can be a condition. These are treated as **False**: `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`. Everything else is **True** (truthy).

```python
name = ""
if name:
    print("has a name")
if not name:
    print("name is empty")      # runs
```

---

## 2. Python elif

`elif` ("else if") checks another condition when the previous `if`/`elif` conditions were False.

```python
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")   # runs
```

**Key points**
- You can have **any number** of `elif` blocks.
- Conditions are checked **top to bottom**; the **first True** one runs and the rest are skipped.

```python
marks = 82
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")        # runs
elif marks >= 50:
    print("Grade C")
```

---

## 3. Python else

`else` catches everything not handled by the previous conditions. It takes **no condition**.

```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")   # runs
```

`else` can also be used directly after `if` (without `elif`):

```python
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")          # runs
```

**Key points**
- `else` must be the **last** block.
- Only **one** `else` is allowed per `if` chain.

---

## 4. Shorthand if

If the body is a single statement, it can be written on the **same line**:

```python
a = 5
b = 2
if a > b: print("a is greater than b")
```

Use this only for very short statements; the normal multi-line form is more readable.

---

## 5. Shorthand if else (ternary)

A one-line `if ... else` that **returns a value** is called the *conditional expression* (ternary operator).

Syntax:

```python
value_if_true if condition else value_if_false
```

```python
a = 2
b = 330
print("A") if a > b else print("B")      # B

result = "Even" if a % 2 == 0 else "Odd"
print(result)                              # Even
```

Chaining multiple conditions on one line:

```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")   # =
```

**Key points**
- Unlike an `if` statement, the ternary form is an **expression**: it can be assigned to a variable or passed to a function.
- The `else` part is **mandatory** here.

---

## 6. Logical operators

Combine multiple conditions.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | True if **both** conditions are True | `a > 1 and b > 1` | `True` only if both hold |
| `or`  | True if **at least one** is True | `a > 1 or b > 1` | `False` only if both fail |
| `not` | **Reverses** the result | `not(a > 1)` | `True` becomes `False` and vice versa |

```python
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")      # runs

if a > b or a > c:
    print("At least one condition is True") # runs

if not a > b:
    print("a is NOT greater than b")        # does not run
```

**Truth tables**

| A | B | A and B | A or B |
|---|---|---------|--------|
| True  | True  | True  | True  |
| True  | False | False | True  |
| False | True  | False | True  |
| False | False | False | False |

**Key points**
- Python uses **short-circuit evaluation**: `and` stops at the first False, `or` stops at the first True.
- Precedence: `not` > `and` > `or`. Use parentheses to be explicit.
- Related operators: comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`), identity (`is`, `is not`) and membership (`in`, `not in`).

```python
fruits = ["apple", "banana"]
if "apple" in fruits and "mango" not in fruits:
    print("OK")
```

- Python also allows **chained comparisons**: `if 1 < x < 10:`.

---

## 7. Nested if

An `if` inside another `if`. The inner block runs only when the outer condition is True.

```python
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")     # runs
    else:
        print("but not above 20.")
else:
    print("10 or less")
```

**Key points**
- Each level needs its own deeper indentation.
- Deep nesting hurts readability. Often it can be flattened with `and`:

```python
if x > 10 and x > 20:
    print("above 20")
```

---

## 8. pass statement

`if` statements **cannot be empty**. An empty body causes a `SyntaxError`. Use `pass` as a placeholder that does nothing.

```python
a = 33
b = 200

if b > a:
    pass        # TODO: implement later
```

**Key points**
- `pass` is a null operation: nothing happens when it executes.
- Also used for empty functions, classes and loops:

```python
def my_function():
    pass

class MyClass:
    pass
```

---

## Quick summary

| Keyword | Purpose |
|---------|---------|
| `if` | Run code if a condition is True |
| `elif` | Check another condition if previous ones were False |
| `else` | Run code when no previous condition was True |
| `x if c else y` | One-line conditional expression |
| `and`, `or`, `not` | Combine / invert conditions |
| nested `if` | `if` inside an `if` |
| `pass` | Empty placeholder block |