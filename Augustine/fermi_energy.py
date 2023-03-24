import numpy as np

def fermi_energy(energies, num_electrons, kt, precision):
    """
    The fermi energy is solved by finding the energy level that has an equal number of
    occupied and unoccupied states.
    
    Args:
    - energies in the form of an array.
    - num_electrons.
    - kt (float) as thermal energy
    - precision (float).
    
    Returns:
    - fermi_energy (float): The Fermi energy of the system.
    """
    
    energies = np.array(energies)
    
    # Define the function that we want to find the root of
    
    def num_occupied_states(E):
        num_occupied = np.sum(np.exp((energies - E) / kt) + 1)**(-1)  # ntotal
       # print(num_occupied + "thus")
        return num_occupied - num_electrons/2

    # Find the energy range that contains the Fermi energy 
    minimum_energy = energies[0]
    maximum_energy = energies[-1]

    # Iterating until we achieve the desired accuracy
    while maximum_energy - minimum_energy > precision: #Always true
        midpoint = (minimum_energy + maximum_energy) / 2
        if num_occupied_states(midpoint) > 0:
            maximum_energy = midpoint
        else:
            minimum_energy = midpoint

    # Return the Fermi energy
    return (minimum_energy + maximum_energy) / 2
    

# Here we define the energy levels of our system as float
energies = [-0.9, -0.82, 0.63, -0.5, -0.31, -0.1, 0.05, 1.3, 2.5, 3.9, 5.5]

# Calculate the number of electrons in the system
num_electrons = 21

# Set the thermal energy to 0.025 eV
kt = 0.025

# Set the desired level of accuracy to 1e-8
precision = 1e-3

# Find the Fermi energy using the bisection algorithm with thermal energy and precision
fermi_E = fermi_energy(energies, num_electrons, kt, precision=precision)

# Print the Fermi energy
print(f"The Fermi energy for {num_electrons} electrons based on {energies} energy levels is: ", fermi_E, "eV")
