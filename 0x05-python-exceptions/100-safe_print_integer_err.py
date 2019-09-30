#!/usr/bin/python3
def safe_print_integer_err(value):

    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print(error.args[0], file=sys.stderr)
        return False
