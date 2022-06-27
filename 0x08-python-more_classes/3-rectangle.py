#!/usr/bin/python3
"""
This is a Rectangle class.
"""


class Rectangle:
    """
       Initialize Rectangle object with height and width.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

    def area(self):
        """function that returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return area printed in hash"""
        _str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                _str += "#"
                if j + 1 == self.__width and i + 1 != self.__height:
                    _str += '\n'
        return _str
