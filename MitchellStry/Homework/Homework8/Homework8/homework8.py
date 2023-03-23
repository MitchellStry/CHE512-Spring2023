"""
Need to solve for equation 7 of Crossing Classified and Corrected Fewest Switches Surface Hopping paper.

H = E(ax[orbital]) ([orbital]+ E(-t[orbaital](k) (k+1 + k +1 [orbital)] + E((1/2)K(x^2)+m(v^2))
molecule is k
x is a vibrational degree of freedom
v is velocity
K is force constant amu/Pa*s^2
m is mass amu
t is hopping amplitude
a is local electron phonon coupling (cm)^-1/(angstroms)
L is length in angstroms
omega is Phonon frequency
g is Electron-phonon coupling strength
N is number of electrons
"""
import math
import numpy as np
f = open("Hamiltonian File", "w+")
import sys
import matplotlib.pyplot as plt
#The below is homeworks 3,5,6.

a=3500.0
K=14500.0
Kb=1.380649*10**-23
T=300.0
gamma=100.0
C=0.1
t= 1.0
L=5.0
m=250.0
#The numbers above are from the literature.
class problemsolving:
    """
    This class solves the hamiltonian.
    """
    def matrixmaking(N,omega):
        """
        This function makes the matrixes.
        Args:
            c (matrix): Fermion opperator
            b (matrix): Phonon opperator
            N (float): number of electrons
            omega1 (float): Frequency
        Returns:
            c (matrix): Fermion opperator
            b (matrix): Phonon opperator
            N (float): number of electrons
            omega1 (float): Frequency
        """
        N=N
        omega1=omega
        c = np.zeros((L,N))
        b = np.zeros((L,))
        return N,omega1,c,b
    def energies (L,N,omega1):
        """
        This function solves the energies.
        Args:
            c[i] (matrix): Fermion opperator
            b[i] (matrix): Phonon opperator
            omega1 (float): Frequency
        Returns:
            K (matrix): The kenetic energy
            V (matrix): The potential energy
        """
        for i in range(L):
            for j in range(N):
                c[i,j] = np.sqrt(2.0/(L+1)) * np.sin((j+1)*np.pi*(i+1)/(L+1))
            b[i] = np.sqrt(1.0/(2.0*omega1)) * (np.sqrt(omega1) * i + 1j)
        K = np.zeros((N*L, N*L)) 
        V = np.zeros((N*L, N*L)) 
        """
        Calculate the matrices for the kinetic and potential energies
        """
    def matrixsolve(L,N,j,i,t,omega1):
        """
        Solves the Matrixes
        Args:
            L (float): length
            N (float): number of electrons
            t (float): Hopping amplitude
            omega1 (float): Frequency
        Returns:
            K (matrix): The kenetic energy
            V (matrix): The potentail energy
        """
        for i in range(L):
            for j in range(N):
                K[i*N+j,i*N+(j+1)%N] = -t
                K[i*N+j,(i+1)%L*N+j] = -t
                K[i*N+j,i*N+j] = omega1*(j+0.5)
                V[i*N+j,i*N+j] = g*b[i]
        return K,V
    def finishedhamil(K,V):
        """
        Solves the Hamiltonian
        Args:
            K (matrix): The kenetic energy
            V (matrix): The potential energy
        Returns:
            H (matrix): The hamiltonian solution
        """
        f.write(F"The solution to the hamiltonian is {H}. \n")
        f.clos
        X=K
        Y=V
        plt.plot(X,Y)
        plt.xlabel("Kenetic Energy")
        plt.ylabel("Potential Energy")
        plt.title("Hamiltonian")
        plt.show()
        H=K+V
        return H
"""
Below is homework 4
"""
kb=1.380649*10**-23
h=6.626*10**-34
me=9.11*10**-31
def fermirootfinder(left,right,number_of_electrons,precision):
    """
    This function should compute the the fermi enegry from the number of electrons.
    Args:
        left (float): A number less than the fermi energy
        right (float): A number more than the fermi energy
        number_of_electrons (float): The number of electrons
        precision (float): The desired degree of accuracy
    Returns:
        Fermie (float): The fermi energy
    """
    ne=number_of_electrons
    Ef=((h**2)/2*me)*((3*(math.pi**2)*ne)**(2/3))             
    levels=[]
    x=0
    while x>left:
        levels.append(right-precision)
        x=x-precision
    Ntot=0
    for x in levels:
        Ntot=levels.index(x)+Ntot
    Fermie=0
    for x in levels:
        ef=ef+(levels.index(x)-Ntot)
        if ef==0:
            Fermie=levels.index(x)
            return Fermie
            break
        if ef<0:
            if (ef+precision)>= 0:
                Fermi=levels.index(x)
                return Fermie
                break
            if ef>0:
                if (ef-precision) <= 0:
                    Fermie=levels.index(x)
                    return Fermie
                    break
