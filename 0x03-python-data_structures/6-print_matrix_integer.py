#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matL in matrix:
            print(' '.join("{:d}".format(matC) for matC in matL))
