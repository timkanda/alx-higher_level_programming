#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            i = char(ord(i) - 32)
        print("{:c}".format(ord(i)), end="")
    print()
