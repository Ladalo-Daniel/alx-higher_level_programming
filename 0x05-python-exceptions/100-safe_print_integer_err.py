#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        # isinstance(value, int)
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
