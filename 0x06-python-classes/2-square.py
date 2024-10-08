#!/usr/bin/python3

"""same class Square"""


class Square:
    """defining the class square"""
    def __init__(self, size=0):
        """initialize a square

        Args:
        size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
