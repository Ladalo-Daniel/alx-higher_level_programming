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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    def my_print(self):

        if self.__size == 0:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end='')

            print()

    @property
    def position(self):
        return (self.__position)

    def positive_tuple(self, tup_list: tuple) -> bool:
        if tup_list[0] < 0 and tup_list[1] < 0:
            return False

        return True

    def valid_len(self, tup_list: tuple) -> bool:
        if len(tup_list) == 2:
            return True

        return False

    def valid_pair(self, tup_list: tuple) -> bool:
        if isinstance(tup_list[0], int) and isinstance(tup_list[1], int):
            return True
        else:
            return False

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or self.positive_tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
