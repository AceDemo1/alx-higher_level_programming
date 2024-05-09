#!/usr/bin/python3
"""
The module define the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    The function returns True if the object is exactly an instance of the
    specified class, otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
