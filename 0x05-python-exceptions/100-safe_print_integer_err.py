#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): integer to print.

    Returns:
        If TypeError or ValueError occurs - False.
        else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
