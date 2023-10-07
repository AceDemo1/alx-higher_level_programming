#!/usr/bin/python3
def uppercase(str):
    for low in str:
        if 'a' <= low <= 'z':
            upper = ord('a') + ord('A')
        else:
            upper = 0
    print("{}".format(chr(ord(low) - upper)), end='')
    print()
