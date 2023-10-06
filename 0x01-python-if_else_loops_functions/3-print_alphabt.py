#!/usr/bin/python3
for ap in range(ord('a'), ord('z') + 1):
    if ap == ord('e') or ord('q'):
        continue
    print('{}'.format(char(ap)))
