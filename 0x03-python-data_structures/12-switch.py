#!/usr/bin/python3
def swap_variables(a, b):
    """Swap the values of two variables."""
    a, b = b, a
    return a, b

a = 89
b = 10
a, b = swap_variables(a, b)
print("a={:d} - b={:d}".format(a, b))
