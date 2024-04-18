#!/usr/bin/python3

import sys
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

def load_from_json_file(filename):
    """This function creates an object from a JSON file
    Args:
    filename: The name of the JSON file
    """

    with open(filename) as file:
        data = json.load(file)
        return data

# Get arguments from the command line excluding the script name
arguments = sys.argv[1:]

# Load existing items from add_item.json if it exists
try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

# Add the new arguments to the existing items
existing_items.extend(arguments)

# Save the updated list to add_item.json
save_to_json_file(existing_items, "add_item.json")
