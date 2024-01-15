#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = [row[:] for row in matrix]
    x = len(z)
    y = len(z[0])

    for i in range(x):
        for j in range(y):
            z[i][j] = z[i][j] ** 2

    return (z)
