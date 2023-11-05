#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for matL in matrix:
        for matC in matL:
            print("{:d}".format(matC), end=" " if matC != matL[-1] else "")
            print()
