#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("Width must be an integer")

        if value < 0:
            raise ValueError("Width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("Height must be an integer")

        if value < 0:
            raise ValueError("Height must be >= 0")

        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        _w = self.__width
        _h = self.__height

        if _w == 0 or _h == 0:
            return 0
        return 2 * (_w + _h)


def __str__(self):
    """Return a string representation of the rectangle."""
    rect = []
    for i in range(self.__height):
        [rect.append('#') for j in range(self.__width)]
        if i != self.__height - 1:
            rect.append("\n")
    return ("".join(rect))

