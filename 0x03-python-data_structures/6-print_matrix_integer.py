#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for matL in matrix:
            print(" ".join("{:d}".format(matC) for matC in matL))
