#!/usr/bin/python3
"""Defines a class square that inherits from rectangle"""

Rec = __import__('9-rectangle').Rectangle


class Square(Rec):
    """Represent a new square"""
    def __init__(self, size):
        """
        Initialize a new
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
