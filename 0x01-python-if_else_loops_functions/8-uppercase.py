#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= i <= 122:
            i = ord(i)
        print("{:c}".format(i), end="")
    print()
