#!/usr/bin/env python3
"""Module that contains a function to update
or add a key/value pair in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair in a dictionary
    and return the updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
