#!/usr/bin/python3
for ap in range(ord('a'), ord('z') + 1):
    if ap == ord('e') or ap == ord('q'):
        continue
    print('{}'.format(chr(ap)))
