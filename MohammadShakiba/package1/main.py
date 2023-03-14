#from mylib.flib import f1, f2, f3
from mylib.flib import *
#import mylib.flib as flib

def printing(called_function, x_min, x_max, dx, filename):
    """
    This function prints the results of function `called_function` for 
    range(x_min, x_max, dx).

    Args:
        called_function (PyObject): The function to be called for printing.
        x_min (float): The x minimum.
        x_max (float): The x maximum.
        dx (float): The spacing between x_min and x_max.
        filename (string): The name of the file in which the results are appended.

    Returns:
        None: This function does not return anything but create some files.
    """
    f = open(filename, 'w') 
    x = x_min

    while x<x_max:
        f.write(F"x = {x}, f = {called_function(x)} \n")
        x += dx 

    f.close() 



#printing( flib.f1, 0, 10, 1.0, 'x1.txt' )
#printing( flib.f2, 0, 10, 1.0, 'x2.txt' )
#printing( flib.f3, 0, 10, 1.0, 'x3.txt' )

printing( f1, 0, 10, 1.0, 'x1.txt' )
printing( f2, 0, 10, 1.0, 'x2.txt' )
printing( f3, 0, 10, 1.0, 'x3.txt' )




