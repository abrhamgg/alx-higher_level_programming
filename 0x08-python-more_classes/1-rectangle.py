#!/usr/bin/python3
"""
This is a Rectangle class.
"""


class Rectangle:
    """
       Initialize Rectangle object with height and width.
    """

    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """get rectangle width
        """
        return self.__width

    @property
    def height(self):
        """rectangle height
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
