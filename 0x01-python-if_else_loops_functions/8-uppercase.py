#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper = ord('a') - ord('A')
        else:
            upper = 0
        print("{}".format(chr(ord(char) - upper)), end='')
    print()
