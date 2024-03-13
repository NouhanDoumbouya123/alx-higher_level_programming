#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))
