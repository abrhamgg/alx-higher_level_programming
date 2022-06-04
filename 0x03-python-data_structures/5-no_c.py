#!/usr/bin/python3
def no_c(string):
    if string is None:
        return
    n = len(string)
    myStr = ""
    tr = "hello"    
    for i in range(0, n):
        c = string[i]
        if c == 'C' or c == 'c':
            continue
        myStr = myStr + c
    string = myStr
    return myStr
