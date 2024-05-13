#!/usr/bin/python3
"""writes to a files"""

def write_file(filename="", text=""):
    """write to file"""
    with open(filename, "w") as f:
        return f.write(text)
