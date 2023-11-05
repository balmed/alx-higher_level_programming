#!/usr/bin/python3
def print_matrix_integer(matrix=[[]])
    for matL in matrix:
        for matC in matL:
            print("{:d}".format(matC), end="\n" if matC != matL[-1] else "")
            print()
