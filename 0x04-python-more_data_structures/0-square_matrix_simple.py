#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the squae value of matrix's integers"""

    return [list(map(lambda x: x ** 2, row)) for row in matrix]
