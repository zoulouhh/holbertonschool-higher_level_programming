#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given divisor and return a new matrix with the results.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): matrix to divide
        div (int/float): divisor

    Returns:
        new list of lists with divided values rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats,
                   or if rows are not of the same size,
                   or if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with rounded results
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix