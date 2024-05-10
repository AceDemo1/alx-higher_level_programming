#!/usr/bin/python3
""" square class """
i = __import__("9-rectangle").Rectangle


class Square(i):
    """ define square class """

    def __init__(self, size):
        """ validate and make size private """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area """
        return self.__size ** 2
