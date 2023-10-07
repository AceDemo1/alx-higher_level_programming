#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if 'a' <= l <= 'z':
            upper = ord('A') - ord('a')
        else:
            upper = 0
        print("{}".format(chr(ord(l) - upper)), end='')
    print()
