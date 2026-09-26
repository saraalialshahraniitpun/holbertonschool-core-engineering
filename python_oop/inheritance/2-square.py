#!/usr/bin/env python3
"""Module that defines a Square class with custom string representation.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A Square class with customized string representation."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the informal string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
