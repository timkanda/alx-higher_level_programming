#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
    if 65 <= i <= 90:
        i = i - 32
    print("{:c}".format(i), end="")
    print()
