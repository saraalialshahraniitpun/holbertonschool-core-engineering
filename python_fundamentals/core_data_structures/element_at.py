#!/usr/bin/env python3
"""Module that contains a function to retrieve
an element from a list safely.
"""


def element_at(my_list, idx):
    """Retrieve an element from a list like in C.
    Return None if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
