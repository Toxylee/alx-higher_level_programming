#!/usr/bin/python3

"""
Module contains a look up function, i.e a function that
returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Function returns list of available
    attributes and methods of an object
    Args:
        obj: The object to look up
    Return: A list of the object's methods and attributes
    """
    return dir(obj)
