class DLL:  # doubly linked list
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}  # {key:node}
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        ans = -1
        if key in self.nodes:
            node = self.nodes[key]
            ans = node.val
            self._remove(node)
            self._append(node)
        return ans

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self._remove(node)
        node = DLL(key, value)
        self._append(node)
        self.nodes[key] = node
        if len(self.nodes) == self.cap + 1:  # len() is O(1)
            first = self.head.nxt  # least recently used
            self._remove(first)
            del self.nodes[first.key]

    def _append(self, node):
        node.pre = self.tail.pre
        node.nxt = self.tail
        self.tail.pre.nxt = node
        self.tail.pre = node

    def _remove(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
