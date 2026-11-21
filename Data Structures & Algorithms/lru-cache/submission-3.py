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
        else:
            if len(self.nodes) == self.cap:
                first = self.head.nxt  # least recently used
                self._remove(first)
                del self.nodes[first.key]
        node = DLL(key, value)
        self._append(node)
        self.nodes[key] = node

    def _append(self, node):
        tmp = self.tail.pre
        tmp.nxt = node
        node.pre = tmp
        node.nxt = self.tail
        self.tail.pre = node

    def _remove(self, node):
        tmp1 = node.pre
        tmp2 = node.nxt
        tmp1.nxt = tmp2
        tmp2.pre = tmp1