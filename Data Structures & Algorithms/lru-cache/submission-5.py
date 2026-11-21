class Node:

    def __init__(self, key, val):
        self.key = key #need both key and val!
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key:Node
        self.head = Node(-1,-1)
        self.tail = Node(-2,-2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        last = self.tail.prev
        last.next = node
        self.tail.prev = node
        node.prev = last
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        elif len(self.cache) == self.capacity:
            first = self.head.next
            self.remove(first)
            self.cache.pop(first.key)
        self.append(node)
        self.cache[key] = node


