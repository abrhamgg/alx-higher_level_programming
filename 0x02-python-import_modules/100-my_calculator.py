#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = argv[2]
        num1 = int(argv[1])
        num3 = int(argv[3])
        if op == '+':
            c = add(int(argv[1]), int(argv[3]))
            print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num3, c))
        elif op == '-':
            c = sub(int(argv[1]), int(argv[3]))
            print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num3, c))
        elif op == "*":
            c = mul(int(argv[1]), int(argv[3]))
            print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num3, c))
        elif op == '/':
            c = div(int(argv[1]), int(argv[3]))
            print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num3, c))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    main()
