#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """A class based on the previous one"""
    def __init__(self, width=0, height=0):
        """The instantiation"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """To retrieve the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """To retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
