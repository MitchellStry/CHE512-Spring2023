# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:17:10 2023

@author: aoben
"""

import numpy as np



def f1(x):
    return x**3 + 4

def f2(x):
    return x**2 + 2*x

def f3(x):
    return np.sin(x)**2


def definite_int( f, a, b, accuracy):
    
    """
    This function computes the definite integral of the function f(X) at the interval of a to b.
    Ags:
        f (PyObject): The function
        a (int): upper limit
        b (int): lower
        accuracy (float): accuracy
    Returns:
        integral_value (float): The value of the integral
    """
    
    
    n = 1     # guess with 1 subinterval
    guess = 0 # Estimate the integral to equal zero
    iteration = 1
    
    while True:
        x = np.linspace(a, b, n+1)  # Divide [a,b] into n rectangles
        y = f(x)                    # Evaluate the function at each rectangle, saving as array
        width = (b-a)/n             # Width of each subinterval

        integral_value = width * (0.5*y[0] + y[1:n].sum() + 0.5*y[n])  # Trapezoidal rule formula
        err = abs(integral_value - guess)
        
        if err < accuracy: # Check for convergence
            break
        
        print(F"iteration number = {iteration}, error ={err},n ={n} approximation = {integral_value}")

        iteration += 1
        n = n * 2    # Double the number of subintervals for the next iteration
        guess = integral_value  # Update the approximation
    exact  = integral_value   
    print(f'exact value = {exact}')   
    return integral_value



definite_int(f1, 0, 3, 1e-10)

print('_________________________________________________________________')

definite_int(f2, 0, 3, 1e-8)

print('_________________________________________________________________')

definite_int(f3, 2*np.pi, -np.pi/2, 1e-7)

print('_________________________________________________________________')




