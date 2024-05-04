#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """A class based on the previous one"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """A method that returns the area
        of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """A methode that returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Return the sring representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print when an object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
