#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv) - 1
    total = 0
    if n == 0:
        print("{:d}".format(total))
    else:
        for i in range(1, n + 1):
            num = int(argv[i])
            total = total + num
        print("{:d}".format(total))


if __name__ == "__main__":
    main()
