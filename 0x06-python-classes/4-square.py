#!/usr/bin/python3
"""class square"""


class Square:
    """private instance"""

    def __init__(self, size=0):
        """initialize the class withe the size instance"""
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """to cal. the area"""
        return (self.__size ** 2)
