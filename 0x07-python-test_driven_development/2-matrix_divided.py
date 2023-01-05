#!/usr/bin/python3

"""2-matrix_divided module

This module has only one function that divides all elements of a matrix.

Example:

>>> matrix_divided = __import__('2-matrix_divided').matrix_divided
>>> matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """ matrix_divided function

    matrix_divided(matrix, div)

    This function receives a list of lists of integers or floats
    Each row of the matrix must be of the same size and div must
    be a number (integer or float) different than 0
    """
    error_list = "matrix must be a matrix (list of lists) of integers/floats"
    new = []
    n_row = []
    row_l = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")

    for row, i in enumerate(matrix):
        n_row = []
        if row_l == 0:
            row_l = len(i)
        elif len(i) != row_l:
            raise TypeError("Each row of the matrix must have the same size")
        for col, j in enumerate(i):
            if type(j) not in [int, float]:
                raise TypeError(error_list)
            else:
                n_row.append(round(j / div, 2))
        new.append(n_row)

    return new
