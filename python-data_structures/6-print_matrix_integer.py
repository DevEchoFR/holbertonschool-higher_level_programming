#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integer in range(len(row)):
            end_characte_list = " " if integer != len(row) - 1 else ""
            print("{:d}".format(row[integer]), end=end_characte_list)
        print()
