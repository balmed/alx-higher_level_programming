#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for matC in matrix:
        print(" ".join("{:d}".format(matL)for matL in matC))
