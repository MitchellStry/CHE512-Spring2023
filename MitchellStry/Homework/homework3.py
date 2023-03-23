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

a=3500
K=14500
m=250
L=5
Kb=1.380649*10**-23
T=300
gamma=100
C=0.1
t= 1.0 
omega0=1.0 
N=5
def Hamiltonian():
    c = np.zeros((L,N), dtype=float)
    b = np.zeros((L,), dtype=float)

if Ei > Ea:
    Eab=Ei-Ea
if Ea> Ei:
    Eab=Ea-Ei

def Wt():

def tau(C,Ekin,Eab):
    tau=hbar*(1+(C/Ekin))/(Eab)
    return tau


def E2():


def hamiltonian(a,vibfree,E2,K,m,v):
    E1=a*vibfree
    H=E1+E2+E3
