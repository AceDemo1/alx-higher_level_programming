#!/usr/bin/python3
def multiple_returns(sentence):
    num = len(sentence)
    if num == 0:
        first = None
    first = sentence[0]
    return (num, first)
