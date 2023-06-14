#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b

    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
