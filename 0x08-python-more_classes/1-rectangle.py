#!/usr/bin/python3
""" Create rectangle class """


class Rectangle:
    """ Define rectangle class """
    def __init__(self, width=0, height=0):
        """ Instantation """
        self.width = width
        self.height = height

    def width(self):
        """ Width """
        return self.__width

    def width(self, value):
        """ Width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

     def height(self):
         """ Height """
        return self.__height

    def height(self, value):
        """ Height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


