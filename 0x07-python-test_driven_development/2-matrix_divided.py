#!/usr/bin/python3
def matrix_divided(matrix, div):
    j = []
    for i in range(len(matrix)):
        l = []
        for k in range(len(matrix[i])):
            l += [matrix[k][i] / div]
        j += [l]
    return j
            

