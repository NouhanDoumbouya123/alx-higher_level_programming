#!/usr/bin/python3

import sys

arguments = sys.argv
length = len(arguments) - 1
print("{} arguments.".format(length))
index = 1
for arg in arguments[1:]:
    print("{}: {}".format(index, arg))
    index += 1
