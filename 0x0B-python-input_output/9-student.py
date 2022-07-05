#!/bin/bash/python3
"""
student class
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """ intialize this class with
        first_name
        last_name
        age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation 
        of python object
        self: object
        """
        return self.__dict__
