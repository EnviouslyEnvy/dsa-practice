class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        # Dummy pointers to tell us least recently and most recently used values
        self.left=Node(0,0)
        self.right=Node(0,0)
        # Left= LRU, right = most recently used
        
        # Initially we want to have these nodes connected to each other. When we add/put a new node we want it to be between these dummy nodes. So this state will not be maintained for long.
        # left <-> right
        self.left.next=self.right
        self.right.prev=self.left

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        nxt.prev=node
        node.next=nxt
        prev.next=node
        node.prev=prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        # remove least recently used.
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
