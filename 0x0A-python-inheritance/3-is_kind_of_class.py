#!/usr/bin/python3
"""
is kind of class
"""


def is_kind_of_class(obj, a_class):
    """function to check if an object an instance of a class
    or instance of a class thats iherited fromm"""
    if isinstance(obj, a_class):
        return True
    return False
