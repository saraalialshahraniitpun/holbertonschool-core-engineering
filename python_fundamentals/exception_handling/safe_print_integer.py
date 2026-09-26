#!/usr/bin/python3
"""Module that contains a function to safely
print an integer value.
"""


def safe_print_integer(value):
    """Print an integer with "{:d}".format() and return True.
    Return False if value is not an integer.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
