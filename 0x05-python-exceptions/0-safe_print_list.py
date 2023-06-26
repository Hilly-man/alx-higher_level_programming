#!/usr/bin/python3

def safe_print_list(my_list, x):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    num_printed = 0
    for i in range(min(x, len(my_list))):
        print("{}".format(my_list[i]), end="")
        num_printed += 1
    print("")
    return num_printed
