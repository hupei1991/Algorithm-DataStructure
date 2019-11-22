class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail

    def __add_to_front(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def __move_to_font(self, node):
        self.__remove_node(node)
        self.__add_to_front(node)

    def __get_last(self):
        if self.tail.prev == self.head:
            return None
        return self.tail.prev

    def __remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.__move_to_font(node)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.__move_to_font(node)
            return
        if len(self.map) == self.capacity:
            last_node = self.__get_last()
            del self.map[last_node.key]
            self.__remove_node(last_node)
        self.map[key] = ListNode(key, value)
        self.__add_to_front(self.map[key])

    def print_map(self):
        map = []
        for key in self.map:
            row = [str(key)]
            node = self.map[key]
            row.append("[key: %s, value: %s]" % (node.key, node.val))
            map.append(': '.join(row))
        print("{ " + ', '.join(map) + " }")

    def print_list(self):
        node = self.head.next
        sb = []
        while node != self.tail:
            sb.append("[key: %s, value: %s]" % (node.key, node.val))
            node = node.next
        print(' -> '.join(sb))

    def print(self):
        self.print_map()
        self.print_list()


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
assert cache.put(3, 3) is None
assert cache.get(2) == -1
assert cache.put(4, 4) is None
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
