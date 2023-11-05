#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listdiv = []
    if my_list is None:
        return None
    for i in my_list:
        if i % 2 == 0:
            listdiv.append(True)
        else:
            listdiv.append(False)
            return listdiv
