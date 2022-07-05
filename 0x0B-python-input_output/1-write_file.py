#!/usr/bin/python3
""" function that write a string to text file"""


def write_file(filename="", text=""):
    """
    function that writes string to a text file and returns the number
    of characters written
    :param filename: input file
    :param text: the text to be written
    :return: number of chars
    """
    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(text)
        return len(text)
