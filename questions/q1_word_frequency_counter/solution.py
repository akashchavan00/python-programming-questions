"""
Q1: Word Frequency Counter
Counts word occurrences in a text, ignoring case and punctuation,
and returns the top N most common words.
"""

import re
from collections import Counter


def get_top_n_words(text, n=5):
    """
    Return the top `n` most frequent words in `text` as a list of (word, count).

    Steps:
    1. Lowercase the text so counting is case-insensitive.
    2. Extract words with a regex, ignoring punctuation.
    3. Count with Counter.
    4. Sort by (-count, word) so the most frequent word comes first,
       and ties are broken alphabetically.
    """
    if not text:
        return []

    normalized = text.lower()
    words = re.findall(r"[a-z']+", normalized)
    # Strip any stray leading/trailing apostrophes produced by punctuation like quotes.
    words = [w.strip("'") for w in words if w.strip("'")]

    counts = Counter(words)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:n]


def main():
    sample_text = (
        "The quick brown fox jumps over the lazy dog. "
        "The dog barks, but the fox doesn't care. "
        "Quick foxes and lazy dogs: a classic story!"
    )

    print("Text:")
    print(sample_text)
    print()

    for n in (3, 5):
        print(f"Top {n} words:")
        for word, count in get_top_n_words(sample_text, n):
            print(f"  {word!r}: {count}")
        print()


if __name__ == "__main__":
    main()
