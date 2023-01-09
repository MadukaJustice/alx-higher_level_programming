#!/usr/bin/python3
"""
    Initialize Module
"""


class MyList(list):
    """
        Class that inherits the 'list' object
    """
    def print_sorted(self):
        """
            function that prints a sorted list (ascending order)
        """
        print(sorted(self))
