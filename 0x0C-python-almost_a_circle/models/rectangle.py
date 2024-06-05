#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, v):
        if type(v) is not int:
            raise TypeError('width must be an integer')
        if v <= 0:
            raise ValueError('width must be > 0')
        self.__width = v

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        if type(v) is not int:
            raise TypeError('height must be an integer')
        if v <= 0:
            raise ValueError('height must be > 0')
        self.__height = v

    @property
    def x(self):
        if x <= 0:
            raise ValueError('x must be >= 0')
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        if y <= 0:
            raise ValueError('y must be >= 0')
        return self.__y

    @y.setter
    def y(self, v):
        self.__y = v
