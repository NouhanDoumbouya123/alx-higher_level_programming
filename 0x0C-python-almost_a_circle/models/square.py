#!/usr/bin/python3
"""This contains a class Square that inherits
from Rectangle class"""

from models.rectangle import Rectangle
"""Importing the Rectangle class
in order to inherit from it"""


class Square(Rectangle):
    """This class is inheriting from Rectangle

    Class Constructor:
    def __init__(self, size, x=0, y=0, id=None)

    Args:
    self: the self
    size: This will replace width and height as
    in they are the same in a square
    x: the new line
    y: the space
    id:the id
    """

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor method that inherit
        everything from the Rectangle class
        excet tihat width and height will have
        the same thing because it is Square"""

        if type(size) is not int:
            raise TypeError("width must be an integer")
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return the string representation"""
        return f"[Square] ({self.id})"\
               f" {self._Rectangle__x}/{self._Rectangle__y} - {self.size}"

    def set_size(self, size):
        """To set the values of width and height"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size  <=  0:
            raise ValueError("size must be > 0")
        self.width = size
        self.height = size

    def get_size(self):
        """This is size getter method"""

        return self.size

    def update(self, *args, **kwargs):
        """Updating the values of the attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self._Rectangle__x = value
                if key == "y":
                    self._Rectangle__y = value

    def to_dictionary(self):
        "This will return the dictionary"""
        return {
                "id": self.id,
                "x": self._Rectangle__x,
                "size": self.size,
                "y": self._Rectangle__y
                }
