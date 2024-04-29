#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    sym = ['.', '?', ':']
    f = 0
    for i in text:
        if f == 1 and i == ' ':
            continue
        if i in sym:
            print(i + '\n\n', end='')
            f = 1
            continue
        print(i, end='')
        f = 0
