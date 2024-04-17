#!/usr/bin/python3
import json
"""THis will return the JSON representation of
an object(string)
"""


def to_json_string(my_obj):
    """This function will return the JSON representation
    of an object of type string
    Args:
    my_obj: The object to be represented

    Returns: JSON representation of an object
    """

    return json.dumps(my_obj)
