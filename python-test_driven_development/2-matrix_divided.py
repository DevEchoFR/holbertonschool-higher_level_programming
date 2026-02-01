#!/usr/bin/python3
"""
Module: matrix_division

This module contains a function that divides all elements
of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix of integers or floats
        div (int or float): Number to divide by

    Returns:
        list of lists: New matrix with divided values

    Raises:
        TypeError: If matrix is not properly structured
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(element, (int, float))
                   for row in matrix
                   for element in row
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

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
