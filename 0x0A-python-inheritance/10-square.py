#!/usr/bin/python3
""" square class """


i = __import__(9-rectangle.py).Rectangle
j = __import__(7-base_geometry.py).BaseGeometry


class Square(Rectangle):
    """ define square class """

    def __init__(self, size):
        """ validate and make size private """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """ area """
        return self.__size ** 2
