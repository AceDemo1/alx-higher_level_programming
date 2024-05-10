#!/usr/bin/python3
""" square class """
i = __import__("9-rectangle").Rectangle


class Square(i):
    """ define square class """

    def __init__(self, size):
        """ validate and make size private """
        super().__init__(size, size)
