#!/usr/bin/python3
"""
    Mod 2-square
    Defines a square by private instance attribute
"""


class Square:
    """Defines a square by private attribute
        Attributes:
            size: Size of the square
    """

    def __init__(self, size=0):
        """
        Initializes the instance / object with optional
        size (integer)
        Args:
            size: Size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0 i.e negavive
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
