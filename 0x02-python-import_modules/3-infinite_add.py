#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = int(len(sys.argv))
    result = 0
    for i in range(1, arg_c):
        result = result + int(sys.argv[i])
    print(result)
