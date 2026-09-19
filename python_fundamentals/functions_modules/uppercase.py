#!/usr/bin/env python3
"""Module for uppercase function."""


def uppercase(str):
    """Print a string in uppercase.

    Args:
        str (str): The string to convert.
    """
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
