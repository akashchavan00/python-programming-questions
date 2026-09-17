"""
Q9: LRU (Least Recently Used) Cache
Implemented with collections.OrderedDict for O(1) get/put.
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._data = OrderedDict()  # front = least recently used, end = most recently used

    def get(self, key):
        if key not in self._data:
            return -1
        # Accessing a key counts as "using" it -> move to the "most recent" end.
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key, value):
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            # popitem(last=False) removes the front item = least recently used.
            evicted_key, _ = self._data.popitem(last=False)
            print(f"  [LRUCache] Evicted key {evicted_key!r} (least recently used)")

    def __repr__(self):
        # Show order from least-recent to most-recent for clarity.
        items = ", ".join(f"{k}={v}" for k, v in self._data.items())
        return f"LRUCache(capacity={self.capacity}, items=[{items}])"


def main():
    cache = LRUCache(capacity=3)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(cache)

    print("get('a'):", cache.get("a"))  # 'a' becomes most recently used
    print(cache)

    cache.put("d", 4)  # capacity exceeded -> evict least recently used ('b')
    print(cache)

    print("get('b'):", cache.get("b"))  # -1, was evicted
    print("get('c'):", cache.get("c"))

    cache.put("c", 30)  # update existing key, also refreshes recency
    print(cache)


if __name__ == "__main__":
    main()
