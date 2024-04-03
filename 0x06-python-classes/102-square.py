#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if one square's area is greater than the other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square's area is greater than or equal to the other's."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if one square's area is less than the other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square's area is less than or equal to the other's."""
        return self.area() <= other.area()
