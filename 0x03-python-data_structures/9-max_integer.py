#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        n = len(my_list)
        if n == 1:
            return my_list[0]

        if n == 2:
            if my_list[0] > my_list[1]:
                return my_list[0]
            else:
                return my_list[1]
        if my_list[0] > my_list[1]:
            maxx = my_list[0]
        maxx = my_list[1]
        for i in range(0, n):
            if my_list[i] > maxx:
                maxx = my_list[i]
        return maxx
    return None
