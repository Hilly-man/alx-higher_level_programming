#!/usr/bin/python3
#0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Print all integers in a list."""
    if my_list is None:
        my_list = []

    for i in range(len(my_list)):
        print(my_list[i])
