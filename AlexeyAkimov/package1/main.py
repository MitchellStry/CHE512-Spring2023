#import mylib.flib
#import mylib.flib as np
#from mylib import flib
#from mylib.flib import f1, f2
from mylib.flib import *


def printing(called_func, x_min, x_max, dx, filename):
    """

    This is a function that prints x and f(x)

    Args:
        called_func (PyObject): this is the function whose values we are going to compute
        x_min (float): minimal value of the argument
        x_max (float): maximal value of the argument
        dx (float): argument increment
        filename (string): the name of the file into which the results are printed out

    Returns:
        None: This function doesn't return anything, but creates some files
    """


    f = open(filename, "w+")

    x = x_min
    while x < x_max:
        f.write(F"x = {x}, f = { called_func(x) }\n")
        x = x + dx

    f.close()


printing( f1, 0.0, 10.0, 1.0,"x.txt")
printing( f2, 0.0, 10.0, 1.0,"x2.txt")


#printing( flib.f1, 0.0, 10.0, 1.0,"x.txt")
#printing( flib.f2, 0.0, 10.0, 1.0,"x2.txt")

#printing( mylib.flib.f1, 0.0, 10.0, 1.0,"x.txt")
#printing( mylib.flib.f2, 0.0, 10.0, 1.0,"x2.txt")
#printing( mylib.flib.f3, 0.0, 10.0, 1.0,"sinx.txt")


#printing( np.f1, 0.0, 10.0, 1.0,"x.txt")
#printing( np.f2, 0.0, 10.0, 1.0,"x2.txt")
