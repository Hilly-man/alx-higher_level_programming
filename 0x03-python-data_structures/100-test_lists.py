import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]

def print_list_info(lst):
    """Print information about a Python list."""
    lib.print_python_list_info(lst)

l = ['hello', 'World']
print_list_info(l)

del l[1]
print_list_info(l)

l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
print_list_info(l)

l = []
print_list_info(l)

l.append(0)
print_list_info(l)

l.append(1)
l.append(2)
l.append(3)
l.append(4)
print_list_info(l)

l.pop()
print_list_info(l)
