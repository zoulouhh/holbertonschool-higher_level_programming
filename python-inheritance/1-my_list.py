#!/usr/bin/python3
"""This module defines the MyList class that inherits from list."""

class MyList(list):
    """Custom list class that adds a print_sorted method."""

    def print_sorted(self):
        """Print the list, but sorted in ascending order."""
        print(sorted(self))
