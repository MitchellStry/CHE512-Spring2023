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
import mylib.flib as fl
f = open(filename, "w+")
import sys
"""
The below is homeworks 3,5,6.
"""
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
    def matrixmaking(N,omega):
        
        N=N
        omega1=omega
        c = np.zeros((L,N))
        b = np.zeros((L,))
    def energies (L,N):
        for i in range(L):
            for j in range(N):
                c[i,j] = np.sqrt(2.0/(L+1)) * np.sin((j+1)*np.pi*(i+1)/(L+1))
            b[i] = np.sqrt(1.0/(2.0*omega1)) * (np.sqrt(omega1) * i + 1j)
        K = np.zeros((N*L, N*L)) 
        V = np.zeros((N*L, N*L)) 
        """
        Calculate the matrices for the kinetic and potential energies
        """
    def matrixsolve(L,N,j,i,t):
        for i in range(L):
            for j in range(N):
                K[i*N+j,i*N+(j+1)%N] = -t
                K[i*N+j,(i+1)%L*N+j] = -t
                K[i*N+j,i*N+j] = omega0*(j+0.5)
                V[i*N+j,i*N+j] = g*b[i]
    def finishedhamil(K,V):
        H = K + V
        f.write(F"The solution to the hamiltonian is {H}. \n")

"""
Below is homework 4
"""
kb=1.380649*10**-23
h=6.626*10**-34
me=9.11*10**-31
def fermirootfinder(left,right,number_of_electrons,precision):
    """
    This function should compute the the fermi enegry from the number of electrons.
    """
    ne=number_of_electrons
    Ef=((h**2)/2*me)*((3*(math.pi**2)*ne)**(2/3))             
    levels=[]
    """
    x=0
    while y>=0:
    print("Input an energy level. Input -1 to end")
    x=float(input())
    if x == -1:
    return levels
    else:
    levels.append(x)
    """
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
