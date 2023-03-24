import numpy as np

def root_finder(f_name, f_params, left, right, precision):
    '''
    Find the root of the function on the interval (left to right) with the specified precision.
    f_name: The function whose root we are looking for.
    f_params (tuple): A tuple of parameters to pass to the function f_name.
    left (float): The left endpoint of the interval to search for a root.
    right (float): The right endpoint of the interval to search for a root.
    precision (float): The desired precision of the root.
    Returns:
    float: The root of the function f_name on the interval (left to right).'''

    while abs(right - left) > precision:
        midpoint = (left + right) / 2
        if f_name(midpoint, f_params[0], f_params[1], f_params[2]) * f_name(left, f_params[0], f_params[1], f_params[2]) < 0:
            right = midpoint
        else:
            left = midpoint
    return (left + right) / 2

def fermi_energy(levels, N, kT):
    '''
    Find the Fermi energy for a system of energy levels and N electrons.
    levels (list): A list of energy levels.
    N (int): The number of electrons.
    kT (float): The thermal energy.
    Returns:
    float: The Fermi energy of the system.'''
    f_params = (levels, N, kT)
    left = min(levels)
    right = max(levels)
    precision = 1e-6
    def f_name(E, levels, N, kT):
        value = 0
        for level in levels:
            value = value + 1 / (1 + np.exp((E - level) / kT))
            return value - N
    return root_finder(f_name, f_params, left, right, precision)


