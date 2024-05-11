#!/usr/bin/python3
"""add attr"""


def add_attribute(ob, attr, va):
    """define func"""

    if not hasattr(ob, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        ob.attr = va
