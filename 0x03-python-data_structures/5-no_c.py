#!/usr/bin/python3
def no_c(string):
    n = len(string)
    for i in range(0, n):
        if i == 'c' or i == 'C':
            string[i] = ''
    return string
