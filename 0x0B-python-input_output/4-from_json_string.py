#!/usr/bin/python3

"""This module contains a function that will return
object(python data structure) represented by a json
"""
import json


def from_json_string(my_str):
    """This function returns the python object representation
    from a json represented object

    Args:
    my_str: the object from json

    Returns:
    return the python representation
    """

    return json.loads(my_str)
