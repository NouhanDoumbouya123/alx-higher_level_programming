#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5
addit = add(10, 5)
sub = sub(10, 5)
mul = mul(10, 5)
div = div(10, 5)

print("{} + {} = {}".format(a, b, addit))
print("{} - {} = {}".format(a, b, sub))
print("{} * {} = {}".format(a, b, mul))
print("{} / {} = {}".format(a, b, div))
