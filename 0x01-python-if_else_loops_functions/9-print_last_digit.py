#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = (-1 * number)
    elif number >= 0:
        number = number
    num = number % 10
    return (num)
