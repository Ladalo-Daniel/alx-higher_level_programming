#!/usr/bin/python3


" This is a class definition or a square."


class Square:
    """This class is a boilerplate for the Square aithemetics.
    The size attribut is made private.

    Args:
        size (int):size of the square to be clalculated.

    Attributes:
        size (int): this attribute of the class is the size
                    of the square with the int datatype.
    """

    def __init__(self, size=0):
        self.__size = size

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
