#!/usr/bin/python3
def matrix_divided(matrix, div):
    j = []
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            j += [matrix[k] / div]
        print(",")
    return j
            

