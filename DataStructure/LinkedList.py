class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "ListNode: " + self.val.__str__()


class LinkedList:
    __head = None
    __length = 0

    def __init__(self, head):
        self.__head = head
        self.__length = self.get_length()

    @classmethod
    def init_with_tuple(cls, *elements):
        dummy = ListNode(0)
        dummy_head = dummy
        for element in elements:
            dummy.next = ListNode(element)
            dummy = dummy.next
        __linked_list = LinkedList(dummy_head.next)
        return __linked_list

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if not self.__head:
            return ""
        ptr = self.__head
        ans_list = []
        while ptr:
            ans_list.append(str(ptr.val))
            ptr = ptr.next
        return " -> ".join(ans_list)

    def __len__(self):
        return self.__length

    def get_length(self):
        """
        get length of the linked list
        :return: int value of the length
        """
        if not self.__head:
            return 0
        length = 0
        ptr = self.__head
        while ptr:
            length += 1
            ptr = ptr.next
        return length

    def get(self, index):
        """
        get value out of the linked list at corresponding index at time: O(n)
        :param index: the index
        :return: the val
        """
        assert 0 <= index < self.__length
        ptr = self.__head
        while index > 0:
            ptr = ptr.next
            index -= 1
        return ptr

    def find(self, val):
        """
        find first node of val at time: O(n)
        :param val: val
        :return: ListNode of the result value, None if found nothing
        """
        ptr = self.__head
        while ptr:
            if ptr.val == val:
                return ptr
            ptr = ptr.next
        return None

    def update(self, index, val):
        """
        put node to the linked list at index at time O(n)
        :param index: index
        :param val: val to be updated
        :return: None
        """
        assert 0 <= index < self.__length
        self.get(index).val = val

    def insert(self, index, val):
        """
        insert a node before index at time complexity of O(n)
        :param index: the index
        :param val: val to be inserted
        :return: None
        """
        assert 0 <= index <= self.__length
        dummy = ListNode(0)
        dummy.next = self.__head
        dummy_head = dummy
        while index > 0:
            dummy = dummy.next
            index -= 1
        node = ListNode(val)
        node.next = dummy.next
        dummy.next = node
        self.__head = dummy_head.next
        self.__length += 1

    def delete(self, index):
        """
        delete the node at index with time O(n), because get time is O(n)
        :param index: the index
        :return: None
        """
        assert 0 <= index < self.__length
        if index == 0:
            self.__head = self.__head.next
            self.__length -= 1
            return
        prev_node = self.get(index - 1)
        prev_node.next = prev_node.next.next


linked_list = LinkedList.init_with_tuple(1, 2, 4, 6, 7)
print(linked_list)
print(linked_list.get(4))
print(linked_list.find(2))
linked_list.update(1, 3)
print(linked_list)
linked_list.insert(4, 3)
print(linked_list)
linked_list.delete(4)
print(linked_list)

