#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') - 1, -1):
    if alpha % 2 != 0:
        conv = 32
    else:
        conv = 0
    print("{}".format(chr(alpha - conv)), end='')
