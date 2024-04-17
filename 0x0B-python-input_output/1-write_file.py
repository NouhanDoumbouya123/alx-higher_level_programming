#!/usr/bin/python3

"""Writing a string to a text file (UTF-8) encoding
and then return the number of character written to it"""


def write_file(filename="", text=""):
    """A function that write a string (text) to a file and then
    return the number of character written
    Args:
    filename: the name of the specific to which the content
    will be written to
    text: The text that will be written to a file

    Return:
    The number of character written to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return file.tell()
