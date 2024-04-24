#!/usr/bin/python3
"""This module contains a class
Rectangle that will inherit from Base"""

from models.base import Base
"""To import the Base class in order
to inherit from it"""


class Rectangle(Base):
    """This is the Rectangle class(child class) from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise TypeError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """To get the width"""

        return self.__width

    @property
    def height(self):
        """To get the height"""

        return self.__height

    @property
    def x(self):
        """To get x"""

        return self.__x

    @property
    def y(self):
        """To get y"""

        return self.__y

    @width.setter
    def width(self, width):
        """To set the width"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """To set the height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """To set x """
        
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """To set y"""

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """This returns the area of a Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """This methode prints to the stdout the Rectangle
        instance with character #"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """This will override teh __str__ method so that it
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id})" \
               f" {self.__x}/{self.__y} -"\
               f" {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """This will update the values of
        the attributes of the Rectangle
        method"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """A method that returns the dictionary
        representation"""
        return {
                "x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width,
                }
