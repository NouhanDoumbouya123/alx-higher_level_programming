#!/usr/bin/python3
""" This function reads a text file and prints it to the standard output
    Args:
    filename
"""


def read_file(filename=""):
    """This function will read a specific file
        Args:
        filename
        Return:
        Nothing
    """
    with open(filename) as file:
        for line in file:
            print(line, end="")
