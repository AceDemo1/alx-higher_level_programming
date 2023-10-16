#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        del = []
        for i in a_dictionary:
                if i == value:
                        del.append(i)
        for i in del:
                del a_dictionary[i]
        return (a_dictionary)
