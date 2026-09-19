#!/usr/bin/env python3
"""Module that contains a function to print all integers of a list."""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for i in my_list:
        print("{:d}".format(i))
