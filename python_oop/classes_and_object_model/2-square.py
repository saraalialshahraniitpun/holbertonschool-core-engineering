#!/usr/bin/env python3
"""Module that defines a Square class with size validation.
"""


class Square:
    """A Square class with size validation in initialization."""

    def __init__(self, size=0):
        """Initialize the square with validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
