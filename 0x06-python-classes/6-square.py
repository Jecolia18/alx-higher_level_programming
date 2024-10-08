#!/usr/bin/python3

"""class square"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize

        Args:
        size (int): size
        position (int, int): The position
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """getter, setter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter"""
        return (self.__position)

    @property
    def position(self):
        """getter n setter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for d in range(0, self.__position[0])]
            [print("#", end="") for f in range(0, self.__size)]
            print("")
