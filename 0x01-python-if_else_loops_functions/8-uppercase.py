#!/usr/bin/python3
def uppercase(str):
    if (ord(str) >= 97) and (ord(str) <= 122):
        str = ord(str) - 32
        print("{str}".format(str=chr(str))
    else:
        print(str)
