#!/usr/bin/python3
def print_last_digit(number):
    number = number % number
    if number < 0:
        number = -(number)
    print(number)
