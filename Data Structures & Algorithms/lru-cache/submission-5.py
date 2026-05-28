# will be using doubly linked list -> need class for nodes
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev, self.next = None, None

class LRUCache:

    # most recently used node - right side
    # least recently used node - left side

    # initialization
    def __init__(self, capacity: int):
        self.capacity = capacity
        # need a hash map that maps key -> node
        self.cache = {}
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # helper - remove
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # helper - insert
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    # if key exists, update value of key
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.left.next # node
            self.remove(LRU)
            del self.cache[LRU.key]
