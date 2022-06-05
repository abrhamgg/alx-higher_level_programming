#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n > 0:
        c = sentence[0]
    else:
        c = None
    tup = (n, c)
    return tup
