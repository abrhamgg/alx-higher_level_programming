#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    n = len(my_list)
    if idx > n - 1:
        return None
    for i in range(0, n):
        if idx == i:
            return my_list[i]
