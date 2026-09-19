#!/usr/bin/env python3
"""Module that contains a function to return
the key with the biggest integer value in a dictionary.
"""


def best_score(a_dictionary):
    """Return the key with the biggest integer value.
    Return None if the dictionary is empty or None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
