#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound."""
        pass


class Dog(Animal):
    """A Dog class inheriting from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """A Cat class inheriting from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
