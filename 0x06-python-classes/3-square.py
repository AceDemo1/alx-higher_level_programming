#!/usr/bin/python3
"""class square"""


class Square:
    """private instance"""

    def __init__(self, size=0):
        """initialize the class withe the size instance"""

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        def area(self):
            """to cal. the area"""
            return (size ** 2)
