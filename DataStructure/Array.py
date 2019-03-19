class Array:
    __elements__ = []
    __length__ = 0

    @classmethod
    def init_with_tuple(cls, *element_tuple):
        __len = len(element_tuple)
        __arr = Array(__len)
        __arr.__elements__ = list(element_tuple)
        __arr.__length__ = __len
        return __arr

    def __init__(self, length):
        """
        constructor
        :param length: length of the array
        """
        assert length >= 1
        self.__elements__ = [0 for _ in range(length)]
        self.__length__ = length

    def __repr__(self):
        return list.__repr__(self.__elements__)

    def __str__(self):
        return list.__str__(self.__elements__)

    def __len__(self):
        return self.__length__

    def get(self, index):
        """
        get element at index at time O(1)
        :param index: index
        :return: the element at index
        """
        assert 0 <= index < self.__length__
        return self.__elements__[0 + index]

    def insert(self, index, element):
        """
        insert element before index at time O(n)
        :param index: index
        :param element: the element tobe inserted
        :return: None
        """
        assert 0 <= index <= self.__length__
        self.__elements__ = self.__elements__ + [0]
        self.__length__ += 1
        for i in range(self.__length__ - 2, index - 1, -1):
            self.__elements__[i + 1] = self.__elements__[i]
        self.__elements__[index] = element

    def find(self, element):
        """
        find the index of corresponding element at time O(n)
        :param element: the element
        :return: the index if found, -1 if not found
        """
        for i in range(self.__length__):
            if element == self.__elements__[0 + i]:
                return i
        return -1

    def update(self, index, element):
        """
        update element at index at time O(1)
        :param index:
        :param element:
        :return:
        """
        assert 0 <= index < self.__length__
        self.__elements__[0 + index] = elemen

    def delete(self, index):
        """
        delete element at index at time O(n)
        :param index: index
        :return: None
        """
        for i in range(index + 1, self.__length__):
            self.__elements__[i - 1] = self.__elements__[i]
        self.__elements__ = self.__elements__[:-1]
        self.__length__ -= 1


arr = Array.init_with_tuple(1, 2, 3)
print(arr)
print("3 is at " + str(arr.find(3)))
arr.insert(3, 4)
print(arr)
arr.delete(2)
print(arr)
arr.update(2, 3)
print(arr)
