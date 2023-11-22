#!/usr/bin/python3


"This is a class definition for a Square with a private variable."


class Square:
    """This class is a boilerplate for the square
    artihmetics. The size attribute is made private.

    Args:
        __size (int): private attribute of the Sqaure class.

    Attributes:
        __size (int): side of the sqaure integer.
    """
    def __init__(self, __size):
        self.__size = __size
