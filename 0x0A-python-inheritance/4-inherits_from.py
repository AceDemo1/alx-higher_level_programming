#!/usr/bin/python3
def inherits_from(obj, a_class):
    if type(obj) is a_class:
        f = 1
    if isinstance(obj, a_class):
        f1 = 1
    if f == 1 and f1 == 1:
        return False
    elif f == 0 and f1 == 1:
        return True
    return False
