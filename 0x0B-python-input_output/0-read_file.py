#!/usr/bin/python3
"""
read_file: function that reads text file and prints it to stdout
"""


def read_file(filename=""):
    """
    function to read a file
    :param filename: input file
    :return: reads the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        read = f.read()
        print(read)
