#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if idx < 0 or idx > n:
        return my_list
    for i in my_list:
        if i == idx:
            my_list.remove(my_list[idx])
    return my_list
