#!/usr/bin/python3
"""
appending to a file
"""


def append_write(filename="", text=""):
    """
    function which appends a string to a text file
    Args:
    filename: input file
    text: string to be added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
