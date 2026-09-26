#!/usr/bin/env python3
"""Module that defines VerboseList extending the built-in list.
"""


class VerboseList(list):
    """A custom list class that prints notifications on modification."""

    def append(self, item):
        """Add an item to the end of the list and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list with items from iterable and print notification."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove the first item from the list and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index (default last) and print notice."""
        # To match exact example outputs where the popped item value is printed:
        # We peek the item before popping it using standard indexing.
        item = self[index]
        super().pop(index)
        print("Popped [{}] from the list.".format(item))
