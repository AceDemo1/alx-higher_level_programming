#!/usr/bin/python3
"""class square"""


class Square:
    """private instance"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the class with the size and position attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if all(type(elem) is not int and elem < 0 for elem in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """calculate the area"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
