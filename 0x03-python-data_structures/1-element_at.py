#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < -len(my_list) or idx >= len(my_list):
        return
    return my_list[idx]
