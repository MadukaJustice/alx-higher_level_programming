#!/usr/bin/python3
"""
    Function definition
"""


def matrix_divided(matrix, div):
    """
        Divides all elements in a matrix by 'div'
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err)

    new_matrix = []
    row_len = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(err)
            new_row.append(round(i/div, 2))
        new_matrix.append(new_row)
    return new_matrix
