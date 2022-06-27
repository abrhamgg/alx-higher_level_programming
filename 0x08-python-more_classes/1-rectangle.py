#!/usr/bin/python3
"""
This is rectangle class
"""


class Rectangle:
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initialize a triangle.
        
        Args:
            width: width of triangle
            height: height of triangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """rectangle height
        """
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigt = value
