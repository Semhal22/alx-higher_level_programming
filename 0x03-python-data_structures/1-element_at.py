#!/usr/bin/python3
def element_at(my_list, idx):
    error = "None"
    if (idx < 0) or (idx > len(my_list) - 1):
        return error
    return my_list[idx]
