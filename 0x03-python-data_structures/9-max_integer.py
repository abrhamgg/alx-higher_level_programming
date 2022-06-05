#!/usr/bin/python3
def max_integer(list=[]):
    if list is None:
        return None
    n = len(list)
    if n == 1:
        return list[0]
    if n == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    if list[0] > list[1]:
        maxx = list[0]
    maxx = list[1]
    for i in range(0, n):
        if list[i] > maxx:
            maxx = list[i]
    return maxx
