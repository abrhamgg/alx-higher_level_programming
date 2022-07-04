#!/usr/bin/python3
"""
Empty class
"""


class BaseGeometry:
    """Base Geometry"""
    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate parameter as integer:
        Args:
            name (str): the name of the parameter
            value (int): The parameter to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", self.__width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", self.__height)
        self.__height = height
