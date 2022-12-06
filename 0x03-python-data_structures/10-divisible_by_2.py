#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    mult_two = list(my_list)
    for i in mult_two:
        if i % 2 == 0:
            mult_two[i] = True
	else:
            mult_two[i] = False
        return mult_two
