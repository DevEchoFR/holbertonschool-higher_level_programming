#!/usr/bin/python3
"""
Module: pascal_triangle
This module contains a function that generates Pascal's triangle.

The function returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): number of rows

    Returns:
        list: Pascal's triangle
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
