#!/usr/bin/python3

"""This module has a function that
creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file
    Args:
    filename: The name of the JSON file
    """

    with open(filename) as file:
        data = json.loads(filename)
        return data
