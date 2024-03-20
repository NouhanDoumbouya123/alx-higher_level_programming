#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    sum_weights = sum(weight for _, weight in my_list)
    weighted_sum = sum(score * weight for score, weight in my_list)
    weighted_avg = weighted_sum / sum_weights

    return weighted_avg
