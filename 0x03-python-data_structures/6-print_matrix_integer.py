#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers."""
    for i in matrix:
        for j in i:
            if j != i[-1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print()
