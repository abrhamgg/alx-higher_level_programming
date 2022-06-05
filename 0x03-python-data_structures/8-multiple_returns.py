#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    c = sentence[0]
    if sentence is None:
        tup = (None)
        return tup
    tup = (n, c)
    return tup
