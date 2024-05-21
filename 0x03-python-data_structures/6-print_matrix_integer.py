#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers."""
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()
