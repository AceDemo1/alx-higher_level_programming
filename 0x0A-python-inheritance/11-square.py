#!/usr/bin/python3
""" square class """
i = __import__("9-rectangle").Rectangle


class Square(i):
    """ define square class """

    def __init__(self, size):
        """ validate and make size private """
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        """ print """
        return f"[Square] {self.__width}/{self.__height}"
