#!/usr/bin/python3
def no_c(my_string):
    my_table = str.maketrans("", "", "cC")
    new_string = my_string.translate(my_table)
    return new_string
