#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    n = len(my_list)
    if idx > n - 1:
        return my_list
    for i in range(0, n):
        if idx == i:
            my_list[i] = element
            return my_list
