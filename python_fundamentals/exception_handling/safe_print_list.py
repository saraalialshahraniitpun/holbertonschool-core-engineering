#!/usr/bin/env python3
"""Module that contains a function to safely
print x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list safely
    and return the real number of elements printed.
    """
    nb_print = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_print += 1
        except IndexError:
            break
    print()
    return nb_print
