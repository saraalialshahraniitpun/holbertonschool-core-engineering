#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Print swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Print flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish using multiple inheritance."""

    def fly(self):
        """Override fly for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat for flying fish."""
        print("The flying fish lives both in water and the sky!")
