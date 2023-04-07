#import mylib.flib
import mylib.flib as fl
#can use more than two letters in name
#can specify which functions using import (filename) as (name) (function 1), (function 2),...
def printing(called_func, x_min, x_max,dx, filename ):
    """
    This is a function that prints x and f(x)

    args:
        called_func (PyObject): this is the function whose values we are going to compute
        x_min (float): minimal value of the argument
        x_max (float): maximal value of the argument
        dx (float): argument increment
        filename (string): the name of the file it prints into

    Returns:
        none: This function doesn't return anything but creates some files
    """
    f = open(filename, "w+")

    x = x_min
    while x < x_max:
        f.write(F"x={x}, f={called_func (x)} \n")
        x = x+dx
    
    f.close()

#printing(mylib.flib.f1,0.0,10.0,1.0,"x.txt")
#printing(mylib.flib.f2,0.0,10.0,1.0,"x2.txt")
#printing(mylib.flib.f3,0.0,10.0,1.0,"sinx.txt")

printing(fl.f1,0.0,10.0,1.0,"x.txt")
printing(fl.f2,0.0,10.0,1.0,"x2.txt")
printing(fl.f3,0.0,10.0,1.0,"sinx.txt")
