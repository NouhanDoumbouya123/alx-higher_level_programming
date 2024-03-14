#!/usr/bin/python3
if __name__ == "__main__":
import sys

arguments = [int(arg) for arg in sys.argv[1:]]
total_sum = 0
for arg in arguments:
    total_sum += arg
print(total_sum)
