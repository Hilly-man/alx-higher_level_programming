#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represent square."""

    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
