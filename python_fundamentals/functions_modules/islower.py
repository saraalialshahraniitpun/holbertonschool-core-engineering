#!/usr/bin/env python3
"""Module for islower function."""


def islower(c):
    """Check if a character is lowercase.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if c is lowercase, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')
