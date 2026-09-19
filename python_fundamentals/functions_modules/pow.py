#!/usr/bin/env python3
"""Module for pow function."""


def pow(a, b):
    """Compute a raised to the power of b.

    Args:
        a (int/float): The base number.
        b (int): The exponent.

    Returns:
        int/float: The result of a to the power of b.
    """
    result = 1
    for _ in range(abs(b)):
        result *= a
    
    if b < 0:
        return 1 / result
    return result
