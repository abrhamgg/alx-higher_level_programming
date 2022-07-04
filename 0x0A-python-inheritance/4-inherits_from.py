#!/usr/bin/python3
"""
inherits from
"""


def inherits_from(obj, a_class):
    """function that returns true if an object is an instance of a
    class that inherited directly or indirectly from class"""
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
