#!/usr/bin/env python3
"""Module that contains a function to safely
print the first x elements of a list, integers only.
"""


def safe_print_list_integers(my_list=[], x=0):
    """Print only integers from the first x elements of a list
    and return the real number of integers printed.
    """
    nb_print = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                nb_print += 1
        except (ValueError, TypeError):
            continue
    print()
    return nb_print
