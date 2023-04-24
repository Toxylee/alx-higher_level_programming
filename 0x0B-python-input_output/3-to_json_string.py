#!/usr/bin/python3

"""
Module contains funtion that returns JSON representation of
an object(string)
"""


def to_json_string(my_obj):
    """Return JSON representation of and object"""
    import json

    return json.dumps(my_obj)
