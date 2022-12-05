#!/usr/bin/env python3
def no_c(my_string):
    new_string = list(my_string)
    index_count = 0
    for idx in new_string:
        if idx == 'c' or idx == 'C':
            new_string[index_count] = ""
            index_count += 1
            return new_string
