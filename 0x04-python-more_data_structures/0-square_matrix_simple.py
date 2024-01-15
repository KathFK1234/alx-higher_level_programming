#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = len(matrix)
    y = len(matrix[0])
    z = matrix.copy()

    for i in range(x):
        for j in range(y):
            matrix[i][j] = matrix[i][j] ** 2

    return (z)
