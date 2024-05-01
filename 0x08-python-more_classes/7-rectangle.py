#!/usr/bin/python3
""" Create rectangle class """


class Rectangle:
    """ Define rectangle class """
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        """ Instantation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Area """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ str """
        if self.__width == 0 or self.__height == 0:
            return ''
        return (Rectangle.print_symbol * self.__width + '\n') * (self.__height - 1) + \
            Rectangle.print_symbol * self.__width

    def __repr__(self):
        """ repr """
        return "Rectangle" + "(" + str(self.__width) + ", " + \
            str(self.__height) + ")"

    def __del__(self):
        """ del """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
