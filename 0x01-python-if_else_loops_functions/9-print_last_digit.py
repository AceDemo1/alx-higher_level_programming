#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = (-1 * number) % 10
        return(-num, end='')
    elif number >= 0:
        num = number % 10
        return(num, end='')
