#!/usr/bin/python3
"""
    2-matrix_divided.py
    This module contains the matrix_dividend function
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of the matrix, and returns a new matrix divided by div
    """
    if type(matrix) not in [list] or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    prev = matrix[0]

    for row in matrix:
        if type(row) not in [list] or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        
        if len(row) != len(prev):
            raise TypeError('Each row of the matrix must have the same size')
        
        prev = row

    if type(div) not in [float, int] or div != div:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_list = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_list.append(new_row)
    return new_list
