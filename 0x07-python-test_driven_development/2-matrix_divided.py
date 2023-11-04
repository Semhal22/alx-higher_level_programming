#!/usr/bin/python3
""" Contains a function matrix_divided """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Arguments:
        matrix: list of lists of integers or floats
        div: a number(integer or float)
    Exceptions:
        TypeError: if matrix or div contains other than numbers
                   if each row of matrix isnot the same size
        ZeroDivisionError: if div is equal to 0
    Return: a new matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise ValueError(msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    len_row = len(matrix[0])
    if not all(len(row) == len_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(element, (int, float))
               for row in matrix
               for element in row):
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
