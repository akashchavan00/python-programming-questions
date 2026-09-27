"""
Q2: Balanced Brackets Validator
Checks whether (), {}, [] are balanced and correctly nested in a string,
ignoring all other characters.
"""


def is_balanced(expression):
    """Return True if all brackets in `expression` are balanced and nested correctly."""
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())
    closing = set(pairs.keys())

    stack = []
    for ch in expression:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        # any other character is ignored

    return len(stack) == 0


def first_unbalanced_index(expression):
    """
    Bonus helper: return the index of the first bracket that breaks balance,
    or None if the expression is balanced. Useful for error messages.
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())
    closing = set(pairs.keys())

    stack = []  # holds (char, index)
    for i, ch in enumerate(expression):
        if ch in opening:
            stack.append((ch, i))
        elif ch in closing:
            if not stack or stack[-1][0] != pairs[ch]:
                return i
            stack.pop()

    if stack:
        return stack[-1][1]  # first unmatched opening bracket
    return None


def main():
    test_cases = [
        "{[a + (b * c)] - d}",
        "([)]",
        "((a+b)",
        "",
        "no brackets here",
        "(((())))",
        "{[()]}[]",
    ]

    for expr in test_cases:
        result = is_balanced(expr)
        print(f"{expr!r:35} -> balanced={result}")
        if not result:
            idx = first_unbalanced_index(expr)
            print(f"{'':35}    first problem at index: {idx}")


if __name__ == "__main__":
    main()
