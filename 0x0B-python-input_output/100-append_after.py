#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """define func"""
    with open(filename, "r") as f:
        k = []
        while True:
            i = f.readline()
            if i == '':
                break
            k += [i]
            if search_string in i:
                k += [new_string]
    with open(filename, "w") as f:
        f.writelines(k)
