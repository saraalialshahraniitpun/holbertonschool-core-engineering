#!/usr/bin/env python3
"""Module that contains a function to print
a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, formatted row by row."""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
