#!/usr/bin/python3
def uppercase(str):
    for low in str:
        if 'a' <= str[low] <= 'z':
            upper = ord('a') + ord('A')
        else:
            upper = 0
    print("{}".format(chr(ord(str[low]) - upper)), end='')
    print()
