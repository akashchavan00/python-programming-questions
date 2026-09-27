# Q1: Word Frequency Counter

## Question
Write a Python program that takes a block of text and returns the N most frequently occurring words, along with their counts. Your solution should:
1. Be case-insensitive ("The" and "the" are the same word).
2. Ignore punctuation.
3. Sort results by frequency (descending). For words with the same frequency, sort alphabetically.
4. Allow the caller to specify how many top words (N) to return.

**Example:**
```
Input text: "The quick brown fox jumps over the lazy dog. The dog barks."
N = 2
Output: [('the', 3), ('dog', 2)]
```

## Approach
1. Normalize the text to lowercase so counting is case-insensitive.
2. Use a regular expression (`re.findall(r"[a-z']+", text)`) to extract words, stripping out punctuation while keeping apostrophes (so contractions like "don't" stay as one word).
3. Use `collections.Counter` to count word occurrences in a single pass.
4. Use `sorted()` with a custom key: a tuple `(-count, word)` so higher counts come first, and ties break alphabetically (ascending).
5. Slice the sorted list down to the top N.

## Concepts Used
- String manipulation and normalization (`str.lower()`)
- Regular expressions (`re` module, `re.findall`)
- `collections.Counter` for frequency counting
- Custom sort keys with `sorted()` and tuple-based tie-breaking
- List slicing
- Functions with default arguments
