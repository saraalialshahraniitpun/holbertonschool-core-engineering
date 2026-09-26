#!/usr/bin/env python3
"""Module that contains a function to divide
two integers safely.
"""


def safe_print_division(a, b):
    """Divide a by b and print the result in finally block.
    Return the result of the division, or None if division fails.
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
