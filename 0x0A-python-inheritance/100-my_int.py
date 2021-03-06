#!/usr/bin/python3
"""class that inherits from int"""


class MyInt(int):
    """
    MyInt
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
