#!/usr/bin/python3
"""add attr"""


def add_attribute(ob, attr, va):
    """define func"""

    if not isinstance(ob, type) and not hasattr(obj, '__slot__'):
        setattr(ob, attr, va)
    else:
        raise TypeError("can't add new attribute")
