#!/usr/bin/python3
"""
Module: 2-matrix_divided
Contains matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div (rounded to 2 decimals)."""

    if type(div) not in (int, float) or div != div or div in (
        float('inf'), float('-inf')
    ):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if any(type(row) is not list or row == [] for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(
                    "matrix must be matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
