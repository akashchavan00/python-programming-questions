# Q2: Balanced Brackets Validator

## Question
Write a function `is_balanced(expression: str) -> bool` that checks whether all brackets `()`, `{}`, `[]` in a given string are balanced and correctly nested. The string may contain other characters (letters, digits, operators) which should be ignored — only the bracket characters matter.

**Examples:**
- `is_balanced("{[a + (b * c)] - d}")` → `True`
- `is_balanced("([)]")` → `False` (wrong nesting order)
- `is_balanced("((a+b)")` → `False` (unmatched opening bracket)

## Approach
1. Use a stack (a plain Python `list`) to keep track of opening brackets as we scan the string left to right.
2. Maintain a dictionary mapping each closing bracket to its matching opening bracket, for O(1) lookups.
3. For every character:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket, check the top of the stack: it must match the corresponding opening bracket, otherwise the expression is unbalanced. Pop it if it matches.
   - Any other character is simply ignored.
4. At the end, the stack must be empty for the expression to be balanced — a non-empty stack means there are unmatched opening brackets left over.
5. As a bonus, `first_unbalanced_index` returns *where* the first problem occurs, which is useful for producing helpful error messages (e.g. in a linter or parser).

## Concepts Used
- Stack data structure using a Python `list` (`append` / `pop`)
- Dictionaries for O(1) lookups
- String iteration and character classification
- Early-exit logic / short-circuit returns
- Writing small, testable functions and covering edge cases (empty string, no brackets, unmatched brackets)
