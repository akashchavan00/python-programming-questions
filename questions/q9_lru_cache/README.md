# Q9: LRU Cache from Scratch

## Question
Implement an `LRUCache` class that supports:
- `LRUCache(capacity)` — initialize with a fixed capacity.
- `get(key)` — return the value if the key exists (and mark it as "recently used"), otherwise return `-1`.
- `put(key, value)` — insert or update the value. If inserting a new key causes the cache to exceed capacity, evict the **least recently used** key first.

Both operations should run in O(1) average time.

## Approach
1. Python's `collections.OrderedDict` remembers insertion order and lets us move an existing key to the end in O(1) with `move_to_end()`, and pop the oldest item in O(1) with `popitem(last=False)`. This makes it a great fit for an LRU cache without hand-writing a doubly linked list.
2. Treat the "end" of the `OrderedDict` as "most recently used" and the "front" as "least recently used."
3. On `get`: if the key exists, call `move_to_end(key)` to mark it as most recently used, then return its value; otherwise return `-1`.
4. On `put`: if the key already exists, update its value and move it to the end. If it's new, insert it; if that pushes the size over capacity, remove the front item with `popitem(last=False)`.
5. Comments in the code explain how this maps to the "textbook" doubly-linked-list + hashmap approach, since that's the design interviewers often expect you to be able to describe even when using `OrderedDict` in practice.

## Concepts Used
- `collections.OrderedDict` (`move_to_end`, `popitem`)
- Designing a class around a clear, minimal public API (`get`/`put`)
- O(1) amortized complexity reasoning
- Cache eviction policies (LRU)
- Dunder methods (`__repr__`) for debugging/inspection
