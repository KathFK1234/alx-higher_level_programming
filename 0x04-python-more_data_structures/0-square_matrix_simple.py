#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = matrix.copy()
    x = len(z)
    y = len(z[0])

    for i in range(x):
        for j in range(y):
            z[i][j] = z[i][j] ** 2

    return (z)
