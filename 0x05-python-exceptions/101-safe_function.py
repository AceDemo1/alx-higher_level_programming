#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
