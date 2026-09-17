# Q8: Anagram Grouping & Palindrome Checker

## Question
1. Write a function `group_anagrams(words)` that groups words that are anagrams of each other. E.g. `["eat", "tea", "tan", "ate", "nat", "bat"]` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` (order within/between groups doesn't matter for correctness).
2. Write a function `is_palindrome(s)` that checks whether a string is a palindrome, ignoring case, spaces, and punctuation (e.g., `"A man, a plan, a canal: Panama"` → `True`), using the **two-pointer technique** (no slicing or reversing the whole string).

## Approach
1. For anagram grouping: two words are anagrams if their sorted characters are identical. Use a `defaultdict(list)` where the key is `''.join(sorted(word))` (a "signature") and the value is the list of words matching that signature — this groups every word in a single O(n · k log k) pass (k = word length), with no nested loops comparing every pair of words.
2. For the palindrome check: filter the string down to lowercase alphanumeric characters, then use two pointers starting at both ends, moving inward and comparing characters; if any mismatch is found, return `False` immediately; if the pointers cross without a mismatch, it's a palindrome.
3. The two-pointer approach avoids allocating a full reversed copy of the string and demonstrates an O(n) approach that stops as early as possible on a mismatch.

## Concepts Used
- `collections.defaultdict` for grouping/bucketing
- Strings as sortable sequences (`sorted(word)` + `''.join`)
- Hashing (using a signature string as a dict key)
- The two-pointer algorithmic technique
- String cleaning with `str.isalnum()` and `str.lower()`
- List comprehensions
