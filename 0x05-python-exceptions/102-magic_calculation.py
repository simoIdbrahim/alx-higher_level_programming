#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for ind in range(1, 3):
        try:
            if ind > a:
                raise Exception('Too far')
            else:
                res += a ** b / ind
        except:
            res = b + a
            break
    return (res)
