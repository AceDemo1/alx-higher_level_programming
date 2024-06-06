#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        return self.__x

    @x.setter
    def x(self, v):
        if type(v) is not int:
            raise TypeError('x must be an integer')
        if v < 0:
            raise ValueError('x must be >= 0')
        self.__x = v

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, v):
        if type(v) is not int:
            raise TypeError('y must be an integer')
        if v < 0:
            raise ValueError('y must be >= 0')
        self.__y = v

    def area(self):
        """define the area"""
        return self.width * self.height

    def display(self):
        """display # on stdout"""
        if self.y:
            print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """overwrite str rep"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """assigns an arg to each attr"""
        if args:
            j = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, j[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """returns dict"""
        return {'id': self.id, 'width': self.width, 'height': \
self.height, 'x': self.x, 'y': self.y}
