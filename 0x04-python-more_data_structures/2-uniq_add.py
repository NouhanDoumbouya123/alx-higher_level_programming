#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = []
    result = 0
    for i in my_list:
        if i in new:
            continue
        else:
            result += i
            new.append(i)
    return result
