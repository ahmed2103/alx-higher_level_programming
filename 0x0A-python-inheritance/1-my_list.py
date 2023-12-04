#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Prints a sorted list of the class"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
