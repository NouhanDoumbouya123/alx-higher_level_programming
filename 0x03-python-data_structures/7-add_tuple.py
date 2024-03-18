#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)
    new_tuple1 = a[0] + b[0]
    new_tuple2 = a[1] + b[1]
    return (new_tuple1, new_tuple2)
