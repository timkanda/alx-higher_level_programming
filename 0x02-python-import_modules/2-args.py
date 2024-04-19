#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    print("{:d} arguments." .format(num_args))
    if num_args == 0:
        print(".", end="\n")
    elif num_args == 1:
        print("argument:", sys.argv[1])
    else:
        print("arguments:")
        for i in range(1, num_args + 1):
            print(i, ":", sys.argv[i])
