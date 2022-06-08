#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newList = []

    def square(x):
        return x ** 2
    for i in matrix:
        newList.append(list(map(square, i)))
    return newList
