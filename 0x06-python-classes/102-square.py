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
        if type(value) is not int
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """to cal. the area"""
        return (self.__size ** 2)

    def __lt__(self, other):
        """Compare if square is less than another by area

        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area

        Args:
            other (Square): square to compare against

        Returns:
            True or False
        """
        return self.size > other.size
