class ListNode:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = ListNode()   # sentinel: next is the most recently used
        self.tail = ListNode()   # sentinel: prev is the least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._remove(node)
        self._add_front(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.v = value
            self._remove(node)
            self._add_front(node)
            return

        node = ListNode(key, value)
        self.key_to_node[key] = node
        self._add_front(node)

        if len(self.key_to_node) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.key_to_node[lru.k]