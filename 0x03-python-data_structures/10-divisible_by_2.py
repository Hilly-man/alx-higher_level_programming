#!/usr/bin/python3
# 10-divisible_by_2.py

def max_integer(my_list=[]):
    """Find the biggest integer in a list."""
    if len(my_list) == 0:
        return None

    max_num = float('-inf')
    for num in my_list:
        if num > max_num:
            max_num = num

    return max_num
