#!/usr/bin/python3
"""add attr"""


def add_attribute(ob, attr, va):
    """define func"""

    if not isinstance(ob, type) and hasattr(ob, '__slot__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(ob, attr, va)
