#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    unc = []
    for i in set_1:
        if i not in set_2:
            unc.append(i)
    for j in set_2:
        if j not in set_1:
            unc.append(j)
    return unc
