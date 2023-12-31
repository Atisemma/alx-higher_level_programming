#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_as_int = int(value)
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
