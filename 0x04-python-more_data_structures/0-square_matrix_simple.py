#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        squares = []
        for row in matrix:
            rowsquared = []
            for x in row:
                rowsquared.append(x ** 2)
            squares.append(rowsquared)
    return squares
