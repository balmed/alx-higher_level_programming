#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listdiv = []
    if my_list:
        return None
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            listdiv.append(True)
        else:
            listdiv.append(False)
            return listdiv
