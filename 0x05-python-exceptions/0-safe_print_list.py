#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index in range(x):
            print(my_list[index], end="")
        print()
        return x
    except IndexError:
        print()
        return index
