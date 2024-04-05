#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
    if 97 <= i <= 122:
        print("{:c}".format(i), end="")
        print()
