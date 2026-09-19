#!/usr/bin/env python3
"""Module for print_last_digit function."""


def print_last_digit(number):
    """Print and return the last digit of a number.

    Args:
        number (int): The number to process.

    Returns:
        int: The last digit of the number.
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
