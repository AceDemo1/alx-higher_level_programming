#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary)
    for i, j in sort.item():
        print("{}: {}".format(i, j))
