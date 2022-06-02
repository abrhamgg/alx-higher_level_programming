#!/usr/bin/python3
for c in range(ord('A'), ord('Z') + 1):
        char = chr(c)
        if char == 'Z':
            print("{:s}".format(char))
            continue
        print("{:s}".format(char), end="")
