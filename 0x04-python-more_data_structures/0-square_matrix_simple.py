#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    maxt = []
    for i in matrix:
        res = list(map(lambda x: x ** 2, i))
        maxt.append(res)
    return (maxt)
