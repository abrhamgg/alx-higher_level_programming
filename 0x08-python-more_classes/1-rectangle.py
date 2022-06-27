#!/usr/bin/python3
"""
This is a Rectangle class.
"""


class Rectangle:
    """
       Initialize Rectangle object with height and width.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for rectangle
        Parameters
        ----------
        width : int
            the width of rectangle object
        height: int
            the height of rectangle object
        """
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
        """
        setter method for width

        Args:
            value : int
            the new width of rectangle object
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """
        setter method for height

        Args:
            value : int
            the height of rectangle object
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
