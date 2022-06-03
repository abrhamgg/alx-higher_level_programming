#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    new = my_list.copy()
    if idx < 0:
        return new
    if idx > n - 1:
        return new
    for i in range(0, n):
        if idx == i:
            new[i] = element
            return new
