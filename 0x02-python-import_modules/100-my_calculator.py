#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        op = {
                '+': add,
                '-': sub,
                '*': mul,
                '/': div
                }
        if argv[2] in op:
        a = int(argv[1])
        b = int(argv[3])
        ops = op[argv[2]]
        res = ops(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
        exit(0)
