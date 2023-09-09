#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0: return
    for i in range(len(my_list)):  
        if (my_list[i] >= 90):
            return my_list[i]
