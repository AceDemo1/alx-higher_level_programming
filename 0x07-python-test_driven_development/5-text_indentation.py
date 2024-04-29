#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    sym = ['.', '?', ':']
    for i in test:
        if i in sym:
            print('\n\n', end='')
            continue
        print(i, end='')
