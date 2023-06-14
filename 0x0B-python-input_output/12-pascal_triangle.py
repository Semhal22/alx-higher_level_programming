#!/usr/bin/python3
"""Module contains function pascal_triangle"""


def pascal_triangle(n):
    """Computes the pascal triangle

    Args:
        int: n
    Returns:
        list of lists
    """
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        my_list.append(temp)
    return my_list
