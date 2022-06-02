#!/usr/bin/python3
from sys import argv
n = len(argv)
print("{:d}: arguments".format(n - 1))
for i in range(1, n):
    print("{:d}: {:s}".format(i, argv[i]))
    if not argv[i]:
        break
