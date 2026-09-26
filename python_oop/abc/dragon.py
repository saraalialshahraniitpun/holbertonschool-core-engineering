#!/usr/bin/env python3
"""Module that demonstrates mixins with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """A mixin providing swimming capability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin providing flying capability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class combining swimming and flying mixins."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
