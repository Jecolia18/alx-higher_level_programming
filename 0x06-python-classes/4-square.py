#!/usr/bin:python3

"""defining a square"""


class Square:
    """the square blueprint"""

    def __init__(self, size=0):
        """initialization

        Args:
        size (int): size square
        """
        self.__size = size

    @property
    def size(self):
        """getter for the size"""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    def area(self):
        """return the area"""
        return (self.__size * self.__size)
