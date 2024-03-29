#!/usr/bin/python3
"""
    Mod 4-square
    Defines a square by private instance attribute
"""


class Square:
    """Defines a square by private attribute
        Attributes:
            size: size of the square
        Methods:
            __init__(self, size=0)
            area(self)
    """

    def __init__(self, size=0):
        """Initializes the instance / object with optional
        size (integer)
        Args:
            size: Size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        getter method
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        setter method
        Args:
            new_size: The new size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0 i.e negavive
        """
        if type(new_size) != int:
            raise TypeError("size must be an integer")

        elif new_size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = new_size

    def area(self):
        """Computes the area of the square by raising size to power of 2
        Returns:
            The area of the square
         """
        return self.__size**2
