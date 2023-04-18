# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:47:14 2023

@author: aoben
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def ode_solver_euler(x0, y0, dx, nsteps):
    
    """
    Args:
        x0 - initial x-coordinate
        y0 - initial y-coordinate
        dx - integration time step
        nsteps - number of steps
        ODE function - dy/dx = 1/x + 3x
    """
    X, Y = [], []
    x, y = x0, y0
    for i in range(nsteps):
        X.append(x)
        Y.append(y)
        
        y = y + dx * (1.0 / x + 3 * x)
        x = x + dx
    return X, Y

def ode_solver_verlet(x0, y0, dx, nsteps):
    """
    Args:
        x0 - initial x-coordinate
        y0 - initial y-coordinate
        dx - integration time step
        nsteps - number of steps
        ODE function - dy/dx = 1/x + 3x
    """
    X, Y = [], []
    x, y = x0, y0
    x_initial = x - dx
    y_initial = y - dx * (1.0 / x0 + 3 * x0)
    for i in range(nsteps):
        X.append(x)
        Y.append(y)
        
        y_final = 2 * y - y_initial + dx ** 2 * (1.0 / x + 3 * x) 
        y_initial = y
        y = y_final
        
        x_initial = x
        x = x + dx
    return X, Y

def exact_solution(x0, y0, X):
    """
    Args:
        x0 - initial x-coordinate
        y0 - initial y-coordinate
        X - array of x-coordinates
    """
    Y = [y0 + np.log(x / x0) + 3 / 2 * (x ** 2 - x0 ** 2) for x in X]
    return Y

x0, y0 = 1.0, 0.0
X = np.linspace(1, 10, 100)
Y_exact = exact_solution(x0, y0, X)
Y_euler = ode_solver_euler(x0, y0, dx=0.09, nsteps=100)[1]
Y_verlet = ode_solver_verlet(x0, y0, dx=0.056, nsteps=100)[1]

plt.plot(X, Y_exact, '*-', label='Exact')
plt.plot(X, Y_euler, label="Euler's method")
plt.plot(X, Y_verlet, label="Verlet method")
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
