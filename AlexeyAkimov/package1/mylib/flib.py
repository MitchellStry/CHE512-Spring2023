"""
.. module:: flib
   :platform: Unix, Windows
   :synopsis: 
       This module implements the functionality to compute Autocorrelation Functions (ACF)
       and do some transformations of them
       The assumption is that data are provided in a matrix form - not vectors, so we can handle the
       data of arbitrary dimensionality


.. moduleauthor:: Alexey V. Akimov

"""

import math

def f1(x):
    """
    
    Linear function

    Args:
        x (float): arument
    
    Returns:
        float: linear function of x 

    """

    return x;

def f2(x):
    return x**2;

def f3(x):
    return (math.sin(x) )**2
