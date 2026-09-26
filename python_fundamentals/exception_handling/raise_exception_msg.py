#!/usr/bin/env python3
"""Module that contains a function to raise
a NameError exception with a custom message.
"""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a message."""
    raise NameError(message)
