#!/usr/bin/python3
"""Defining a class Square based on the previous"""


class Square:
    """A square with instantiation and attribute"""

    def __init__(self, size=0):
        """Initialize a new Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
