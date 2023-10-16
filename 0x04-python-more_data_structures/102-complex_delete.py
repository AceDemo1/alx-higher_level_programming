#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dele = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            dele.append(i)
    for i in dele:
        del a_dictionary[i]
    return (a_dictionary)
