#!/usr/bin/python3

"""This module contains a function that writes
an object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """This function will write the object(my_obj)
    to the file(filename)

    Args:
    my_obj: The object that will be written to a file
    filename: The name of the file to write to
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
