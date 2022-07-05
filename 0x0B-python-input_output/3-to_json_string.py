#!/usr/bin/python3
""" importing json lib"""
import json
"""
To JSON string
"""


def to_json_string(my_obj):
    """
    function the changes a python object to json string
    my_obj: input obj
    return: json string
    """
    jn = json.dumps(my_obj)
    return jn
