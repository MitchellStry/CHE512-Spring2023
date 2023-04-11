import numpy as np
import math

def error(E_f, params):
    """

    Args:
      E_f (float): Fermi energy [units: eV]. Assume all levels are singly-occupied (spin-orbitals)
      params["E"] (float numpy array): energy levels [unit: eV]
      params["number_of_electrons"] (int): the actual number of electrons
      params["kbT"] (float): Fermi-Dirac smearing [units: eV]

    Returns:
      float: difference between the total number of electrons according the Fermi-Dirac 
              distribution with Fermi energy E_f and the actual number of electrons

    """

    E = params["E"]
    kbT = params["kbT"]
    N = params["number_of_electrons"]

    tot_pop = 0.0
    for e_i in E:
        pop_i = 1.0 + math.exp( (e_i - E_f)/ kbT )
        pop_i = 1.0 / pop_i  

        tot_pop = tot_pop + pop_i

    return tot_pop - N

def occupations(E_f, params):

    E = params["E"]
    kbT = params["kbT"]

    for e_i in E:
        pop_i = 1.0 + math.exp( (e_i - E_f)/ kbT )
        pop_i = 1.0 / pop_i

        print(F" energy = {e_i},  population = {pop_i}")




def sign(x):
    res = 0.0
    if x>0.0:
        res = 1.0
    elif x<0.0:
        res = -1.0

    return res



def root_finder(f, f_params, x_min, x_max, precision):
    """
    Finds a root of a 1D function on an interval
  
    Args:
      f (PyObject): the function whose root we are looking for 
      f_params (dict): the parameters of that function
      x_min (float): left boundary of the interval
      x_max (float): right boundary of the interval
      precision (float): maximal value of the constraining interval
    
    Returns:
      float: the position of the root of the function f

    """

    err =  2.0 * precision

    x_l, x_r = x_min, x_max
    x_m = (x_l + x_r)/2.0
   
    cnt = 0 
    while err > precision and cnt<25:
        x_m = (x_l + x_r)/2.0

        s_l = sign( f(x_l, f_params) )
        s_m = sign( f(x_m, f_params) )
        s_r = sign( f(x_r, f_params) )

        print(x_l, x_m, x_r, s_l, s_m, s_r)

        if s_l * s_m <= 0.0:
            x_r = x_m

        if s_r * s_m <= 0.0:
            x_l = x_m 

        err = abs(x_l - x_r)
        cnt = cnt + 1


    return x_m



def f1(x, params):
    return x 
    
def f2(x, params):
    return x*x - 1.0


root = root_finder(f1, {}, -2.0, 1.0, 1.3e-10)
print(root)

root = root_finder(f2, {}, -2.1, 0.0, 1e-3)
print(root)

root = root_finder(f2, {}, -0.10, 2.0, 1e-3)
print(root)


params = {}

# Here we define the energy levels of our system as float
params["E"] = [-0.9, -0.82, 0.63, -0.5, -0.31, -0.1, 0.05, 1.3, 2.5, 3.9, 3.9, 4.5]

# Calculate the number of electrons in the system
params["number_of_electrons"] = 10

# Set the thermal energy to 0.025 eV
params["kbT"] = 0.025

# Set the desired level of accuracy to 1e-8
precision = 1e-3

# Find the Fermi energy using the bisection algorithm with thermal energy and precision
fermi_E = root_finder(error, params, params["E"][0], params["E"][-1], precision)

# Print the Fermi energy
N = params["number_of_electrons"]
E = params["E"]
print(f"The Fermi energy for {N} electrons based on {E} energy levels is: ", fermi_E, "eV")

occupations(fermi_E, params)
