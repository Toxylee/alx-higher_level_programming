#!/usr/bin/python3

"""
Module contains class that inherit another class
and in this case, class list.
"""


class MyList(list):
    """Class inherits the default list class
    Args:
        list: The parent or base class
    Attributes:
        print_sorted - Print the list in sorted (ascending order)
        without mutating the original list
    """
    def print_sorted(self):
        """Print list in ascending other without mutating"""
        print(sorted(self))
