#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {key: i * 2 for key, i in a_dictionary.items()}
    return new
