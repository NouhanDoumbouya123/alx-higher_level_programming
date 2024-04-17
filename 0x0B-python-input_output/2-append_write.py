#!/usr/bin/python3

"""This is going to append a text at the end of a file,
or create a new file if it does not exist"""


def append_write(filename="", text=""):
    """This function is going to append a text to a file
    or create a new one if it does not exist
    Args:
    filename:The name of the file
    text: The text to be appended

    Return:
    The number of character appended
    """
    with open(filename, "a+", encoding="utf-8") as file:
        # Its current position
        current = file.tell()

        # Appending text to the file
        file.write(text)

        # Ending position
        end = file.tell()
        
        # Number of characters written is:
        num = end - current

        return num

