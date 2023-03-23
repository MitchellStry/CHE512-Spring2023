"""
Need to solve for equation 7 of Crossing Classified and Corrected Fewest Switches Surface Hopping paper.

H = E(ax[orbital]) ([orbital]+ E(-t[orbaital](k) (k+1 + k +1 [orbital)] + E((1/2)K(x^2)+m(v^2))
molecule is k
x is a vibrational degree of freedom
v is velocity
K is force constant amu/Pa*s^2
m is mass amu
-t is electronic coupling
a is local electron phonon coupling (cm)^-1/(angstroms)
L is length in angstroms
"""
import math

a=3500
K=14500
m=250
L=5
Kb=1.380649*10**-23
T=300
gamma=100
Ei=
Ea=
Eab=0
C=0.1

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
