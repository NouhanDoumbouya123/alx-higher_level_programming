#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) >= 97) and (ord(char) <= 122):
            str = ord(str) - 32
            print("{str}".format(str=chr(str))
        else:
            print(str)
