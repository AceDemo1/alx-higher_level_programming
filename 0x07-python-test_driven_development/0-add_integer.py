#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Return the addition of two numbers."""
    if type(a) is not int or type(a) is not int:
        raise TypeError('a must be an integer')
    a = int(a)
    b = int(b)
    return a + b

