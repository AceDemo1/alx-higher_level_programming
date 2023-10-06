#!/usr/bin/python3
def uppercase(str):
    for low in str:
        if 'a' <= low <= 'z':
            upper = ord(low) - ord('a') + ord('A')
            print("{}".format(chr(upper)), end='')
        else:
            print("{}".format(low), end='')
    print()
