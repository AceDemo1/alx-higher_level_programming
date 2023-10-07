#!/usr/bin/python3
def uppercase(str):
    for l in range(len(str)):
        if ord('a') <= ord(str[l]) <= ord('z'):
            upper = ord('a') - ord('A')
        else:
            upper = 0
        print("{}".format(chr(ord(str[l]) - upper)), end='')
    print()
