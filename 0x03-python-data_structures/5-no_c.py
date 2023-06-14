#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    copy = ''.join([x for x in my_string if x.lower() != 'c'])
    return (copy)
