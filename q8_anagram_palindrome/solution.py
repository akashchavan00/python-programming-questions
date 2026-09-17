"""
Q8: Anagram Grouping & Palindrome Checker
Demonstrates hashing/grouping with defaultdict and the two-pointer technique.
"""

from collections import defaultdict


def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = defaultdict(list)
    for word in words:
        signature = "".join(sorted(word.lower()))
        groups[signature].append(word)
    return list(groups.values())


def is_palindrome(s):
    """
    Check if `s` is a palindrome, ignoring case, spaces, and punctuation.
    Uses the two-pointer technique instead of reversing the string.
    """
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "silent"]
    print("Words:", words)
    print("Anagram groups:")
    for group in group_anagrams(words):
        print(" ", group)

    test_strings = [
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "Hello, World!",
        "",
        "Madam, I'm Adam",
    ]

    print("\nPalindrome checks:")
    for s in test_strings:
        print(f"  {s!r:35} -> {is_palindrome(s)}")


if __name__ == "__main__":
    main()
