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
        result = term1 + term2
    elif sys.argv[2] == "-":
        result = term1 - term2
    elif sys.argv[2] == "*":
        result = term1 * term2
    else:
        if term2 == 0:
            print("Division is not possible")
            exit(0)
        result = term1 / term2
    print("{} {} {} = {}".format(term1, sys.argv[2], term2, result))
