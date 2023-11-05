#!/usr/bin/python3
def max_integer(my_list=[]):
    list_copy = my_list.copy()
    if len(my_list) == 0:
        return None
    list_copy.sort()
    return list_copy[-1]

