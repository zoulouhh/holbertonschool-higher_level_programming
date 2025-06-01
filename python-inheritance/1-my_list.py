#!/usr/bin/python3
"""This module creates a special list that can sort itself."""


class MyList(list):
    """A list that knows how to order itself."""

    def print_sorted(self):
        """Displays the list by arranging numbers from smallest to largest."""
        print(sorted(self))
