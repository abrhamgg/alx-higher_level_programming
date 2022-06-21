#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """initialize the Square class
        Args:
            size: the size of new square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """function to print the square in '#'"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
                if j + 1 == self.__size:
                    print()
