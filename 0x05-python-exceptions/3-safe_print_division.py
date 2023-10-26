#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a / b
    except Exception:
        r = None
    finally:
        print("Inside result:{}".format(r))
    return (r)


