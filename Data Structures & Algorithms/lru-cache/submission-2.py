class LL:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyNode = {}
        self.head = LL(-1, -1)
        self.tail = LL(-2, -2)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.keyNode:
            node = self.keyNode[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyNode:
            node = self.keyNode[key]
            node.val = value
            self.remove(node)
        else:
            node = LL(key, value)
            if len(self.keyNode) == self.cap:
                last = self.tail.pre
                self.remove(last)
                del self.keyNode[last.key]
            self.keyNode[key] = node
        self.insert(node)

    def insert(self, node):
        node.pre = self.head
        node.nxt = self.head.nxt
        self.head.nxt.pre = node
        self.head.nxt = node

    def remove(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre


