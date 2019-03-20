from abc import *


class Stack:
    # Abstract Data Type
    @property
    @abstractmethod
    def is_empty(self):
        ...

    def is_full(self):
        ...

    def peek(self):
        ...

    def push(self, val):
        ...

    def pop(self):
        ...


class ArrayStack(Stack):
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = -1
        self.arr = [0] * self.max_size

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.arr.__str__()

    def is_empty(self):
        """
        identify if the stack is empty at time O(1)
        :return: Boolean value
        """
        if self.top == -1:
            return True
        return False

    def is_full(self):
        """
        identify if the stack is full at time O(1)
        :return: Bool
        """
        if self.top >= self.max_size - 1:
            return True
        return False

    def peek(self):
        """
        peek the first value of the stack at time O(1)
        :return: the value at the top of the stack
        """
        if self.is_empty():
            return None
        return self.arr[self.top]

    def push(self, val):
        """
        push the value into the stack at time O(1)
        :param val: the value
        :return: None
        """
        if not self.is_full():
            self.top += 1
            self.arr[self.top] = val

    def pop(self):
        """
        pop out the top value at time O(1)
        :return: the value
        """
        if not self.is_empty():
            ans = self.arr[self.top]
            self.arr[self.top] = 0
            self.top -= 1
            return ans


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "ListNode: %s" % self.val


class LinkedListStack(Stack):
    def __init__(self):
        self.head = ListNode(0)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        ptr = self.head
        ans_list = []
        while ptr:
            ans_list.append(str(ptr.val))
        return " -> ".join(ans_list)

    def is_full(self):
        """
        identify if the stack is full or not in time O(1)
        :return: bool
        """
        return False

    def is_empty(self):
        """
        identify if the stack is empty or not in time O(1)
        :return: bool
        """
        return self.head.next is None

    def peek(self):
        """
        return the top-of-stack value in time O(1)
        :return: value, else None
        """
        if not self.is_empty():
            return self.head.next.val
        return None

    def push(self, val):
        """
        add value on the top of the stack, the next value of the head in this data structure
        :param val: the val
        :return: None
        """
        if not self.is_full():
            node = ListNode(val)
            node.next = self.head.next
            self.head.next = node

    def pop(self):
        """
        pop out the top-of-stack value in time O(1)
        :return: the value else None
        """
        if not self.is_empty():
            ans = self.head.next.val
            self.head.next = self.head.next.next
            return ans


def test(stack):
    print("-----------------------------------------")
    print("Stack is Empty: %s" % stack.is_empty())
    print("Pushing 1")
    stack.push(1)
    print("Stack is Empty: %s" % stack.is_empty())
    print("Peeking top: %s" % stack.peek())
    print("Pushing 2")
    stack.push(2)
    print("Pushing 3")
    stack.push(3)
    print("Pushing 4")
    stack.push(4)
    print("Stack is Full: %s" % stack.is_full())
    print("Peeking top: %s" % stack.peek())
    print("Popping %s" % stack.pop())
    print("Peeking top: %s" % stack.peek())
    print("Popping %s" % stack.pop())
    print("Popping %s" % stack.pop())
    print("Stack is Empty: %s" % stack.is_empty())


test(ArrayStack(3))
test(LinkedListStack())
