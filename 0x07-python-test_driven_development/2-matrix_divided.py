#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    m = 'matrix must be a matrix (list of lists) of integers/floats'
    m2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(m)
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    j = []
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(m)
        if i == 0:
            count = len(matrix[i])
        elif count != len(matrix[i]):
            raise TypeError(m2)
        matx = []
        for k in range(len(matrix[i])):
            if type(matrix[i][k]) is not int and \
            type(matrix[i][k]) is not float:
                raise TypeError(m)
            matx += [round(matrix[i][k] / div, 2)]
        j += [matx]
    return j
