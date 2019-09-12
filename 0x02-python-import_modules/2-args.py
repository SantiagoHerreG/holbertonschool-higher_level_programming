#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = int(len(sys.argv))
    if arg_c == 1:
        print("0 arguments.")
    elif arg_c == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(arg_c - 1))
    for i in range(1, arg_c):
        print("{0:d}: {1:s}".format(i, sys.argv[i]))
