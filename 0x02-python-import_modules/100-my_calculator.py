#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    arg_c = int(len(sys.argv))

    if arg_c != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (sys.argv[2] in ("+", "-", "/", "*")) is False:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    term1 = int(sys.argv[1])
    term2 = int(sys.argv[3])

    if sys.argv[2] == "+":
        res = term1 + term2
    elif sys.argv[2] == "-":
        res = term1 - term2
    elif sys.argv[2] == "*":
        res = term1 * term2
    else:
        if term2 == 0:
            print("{0:d} / {1:d} = Not possible".format(term1, term2))
            exit(1)
        res = term1 / term2

    print("{0:d} {1:s} {2:d} = {3:d}".format(term1, sys.argv[2], term2, res))
