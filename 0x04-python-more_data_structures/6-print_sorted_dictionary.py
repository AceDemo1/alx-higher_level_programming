#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.item())
    for i, j in sort:
        print("{}: {}".format(i, j))
