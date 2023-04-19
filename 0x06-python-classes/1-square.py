#!/usr/bin/python3
"""
    Mod 1-square
    Defines a square by private instance attribute
"""


class Square:
    """Defines a square by private attribute
        Attributes:
            size: Size of the square
    """

    def __init__(self, size):
        """
        Initializes the instance / object with
        size (no type / value verification)
        Args:
            size: Size of the square
        """
        self.__size = size
