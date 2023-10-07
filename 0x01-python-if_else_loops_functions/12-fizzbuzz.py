#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end='')
        if num % 3 == 0:
            print("Fizz ", end='')
        elif num % 5 == 0:
            print("Buzz ", end='')
        else:
            print(num, end=' ')
