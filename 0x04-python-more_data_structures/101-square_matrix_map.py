#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    square = lambda x: x ** 2

    squared_matrix = [[square(x) for x in row] for row in matrix]
    return squared_matrix
