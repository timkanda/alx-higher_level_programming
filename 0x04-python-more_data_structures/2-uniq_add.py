#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    res = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
        for uniques in new_list:
            res += uniques
        return res
