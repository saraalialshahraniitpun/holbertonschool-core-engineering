#!/usr/bin/env python3
"""Module that contains a function to add two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples, returning a new
    tuple with two integers.
    Missing values are treated as 0,
    and values beyond the first two are ignored.
    """
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]

    return (a[0] + b[0], a[1] + b[1])
