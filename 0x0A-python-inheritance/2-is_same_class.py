#!/usr/bin/python3
"""
is_same_class
"""


def is_same_class(obj, a_class):
    """function to check if an object is an exact instant of class"""
    if type(obj) == a_class:
        return True
    else:
        return False
