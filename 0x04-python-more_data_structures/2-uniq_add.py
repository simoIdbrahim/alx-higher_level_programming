#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqNum = set(my_list)
    number = 0
    for i in uniqNum:
        number += i
    return number
