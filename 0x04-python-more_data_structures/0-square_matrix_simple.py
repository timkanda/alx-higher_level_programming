#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    new_matrix = list(map(lambda n: n ** 2, matrix[]))
    return new_matrix
