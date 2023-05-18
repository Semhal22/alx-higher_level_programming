#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), ([element for element in row] for row in matrix)))

