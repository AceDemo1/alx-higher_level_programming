#!/usr/bin/python3
"""
The module define the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    f = 0
    f1 = 0
    if type(obj) is a_class:
        f = 1
    if isinstance(obj, a_class):
        f1 = 1
    if f == 1 and f1 == 1:
        return False
    elif f == 0 and f1 == 1:
        return True
    return False
