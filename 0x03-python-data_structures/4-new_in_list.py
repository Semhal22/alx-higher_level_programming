#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = []
    for num in my_list:
        list_copy.append(num)
    if (idx < 0) or (idx > len(list_copy) - 1):
        return list_copy
    list_copy[idx] = element
    return list_copy
