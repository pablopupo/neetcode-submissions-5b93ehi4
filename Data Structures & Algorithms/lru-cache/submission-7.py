class Node:
    def __init__ (self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.capacity = capacity
        self.cache = {}

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = node.prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        node.prev = prev
        prev.next = node

        node.next = nxt
        nxt.prev = node

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

        lru = self.left.next
        if len(self.cache) > self.capacity:
            self.remove(lru)
            del self.cache[lru.key]
            