#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """define func"""
    with open(filename, "a") as f:
        return f.write(text)
