#!/usr/bin/python3
def uppercase(str):
    if (ord(str) >= 97) and (ord(str) <= 122):
        str = chr(ord(str) - 32)
        print(str)
    else:
        print(str)
