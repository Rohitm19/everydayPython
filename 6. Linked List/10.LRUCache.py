#vsCode

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Manual input and usage
cache = LRUCache(2)  # Create an LRUCache with a capacity of 2

# Put key-value pairs into the cache
cache.put(1, 1)
cache.put(2, 2)

# Retrieve values from the cache
print("Value for key 1:", cache.get(1))  # Should print 1
print("Value for key 2:", cache.get(2))  # Should print 2

# Put a new key-value pair, which will evict the least recently used key (key 1)
cache.put(3, 3)

# Try to retrieve the evicted key (key 1)
print("Value for key 1 after eviction:", cache.get(1))  # Should print -1 (key 1 is no longer in the cache)
