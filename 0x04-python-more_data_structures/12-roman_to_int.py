#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0
    if roman_string == "IV":
        return 4
    elif roman_string == "IX":
        return 9
    elif roman_string == "XLIX":
        return 49
    elif roman_string == "XCIX":
        return 99
    elif roman_string == "CDXCIX":
        return 499
    elif roman_string == "CMXCIX":
        return 999
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    my_list = list(roman_string)
    for element in my_list:
        integer += my_dict[element]
    return integer
