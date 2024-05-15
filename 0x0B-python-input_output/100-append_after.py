#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as f:
        k = []
        while True:
            i = f.readline()
            if i == '':
                break
            k += i
            for j in i:
                if j == search_string:
                    k += new_string
    with open(filename, "w") as f:
        f.writelines(k)
