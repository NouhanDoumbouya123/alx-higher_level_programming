#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    # Define the square function outside the function
    square = lambda x: x ** 2

    # Use map function within list comprehension to square each element of each row
    squared_matrix = [list(map(square, row)) for row in matrix]

    return squared_matrix
