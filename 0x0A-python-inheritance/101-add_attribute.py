#!/usr/bin/python3
"""add attr"""


def add_attribute(ob, attr, va):
    """define func"""

    if not isinstance(ob, type):
        raise TypeError("can't add new attribute")
    setattr(ob, attr, va)
