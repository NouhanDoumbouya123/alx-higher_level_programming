#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big = float('-inf')
    cle = None

    for key, value in a_dictionary.items():
        if value is not None:
            if  value > big:
                big = value
                cle = key
    return cle

