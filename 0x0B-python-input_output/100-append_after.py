#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, "a") as f:
        while True:
            i = f.readline()
            for j in i:
                if j == search_string:
                    i += new_string
                    break
