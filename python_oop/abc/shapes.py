#!/usr/bin/env python3
"""Module that defines Shape abstract base class, Circle, Rectangle,
and duck typing shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """An abstract base class representing geometric shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """A Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """A Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of a given shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
