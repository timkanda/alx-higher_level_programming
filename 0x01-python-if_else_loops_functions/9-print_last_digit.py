#!/usr/bin/python3
def print_last_digit(number):
    for ld in number:
        ld = ord(i)
    ld = number % 10 if number >= 0 else number * (-1) % 10
    if number < 0:
        ld = -int(ld)
    print(number, end="")
    print(ld)
