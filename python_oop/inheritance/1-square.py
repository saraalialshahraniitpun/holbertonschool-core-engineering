#!/usr/bin/env python3
"""Module that defines a Square class inheriting from Rectangle.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A Square class defined by size."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
