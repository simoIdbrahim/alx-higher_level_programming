a#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max = max(list_num)

    for i in list_num:
        if max > i:
            sub += i

    return (max - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    number = 0
    rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= rom:
                    number += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))

                rom = rom_n.get(ch)

    number += to_subtract(list_num)

    return (number)

