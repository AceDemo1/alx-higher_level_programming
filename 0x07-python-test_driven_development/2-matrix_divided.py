#!/usr/bin/python3
def matrix_divided(matrix, div):
    j = []
    for i in range(len(matrix)):
        l = []
        for k in range(len(matrix[i])):
            l += [round(matrix[k][i] / div, 2)]
        j += [l]
    return j
            

