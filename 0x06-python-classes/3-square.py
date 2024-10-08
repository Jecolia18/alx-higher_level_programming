#!/usr/bin/python3

"""square"""


class Square:
    """square blueprint"""

    def __init__(self, size=0):
        """initialize the square

        Args: size (int): The size of square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """return the square area"""
        return (self.__size * self.__size)
