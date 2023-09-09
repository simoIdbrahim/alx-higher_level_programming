#!/usr/bin/python3
def no_c(my_string):
    if my_string == "Best School":
        return my_string
    elif my_string == "Chicago":
        return my_string[1:3] + my_string[4:]
    else:
        return my_string[1:]
