#!/usr/bin/python3
"""
print sorted list
"""


class MyList(list):
    """MyList inherits from the class list"""

    def print_sorted(self):
        print(sorted(self))
