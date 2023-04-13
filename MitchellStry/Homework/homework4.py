import math
import sys

def fermirootfinder(left,right,number_of_electrons,precision):
    """
    This function should compute the the fermi enegry from the number of electrons.
    """
    kb=1.380649*10**-23
    h=6.626*10**-34
    me=9.11*10**-31

    ne=number_of_electrons
    ef=((h**2)/2*me)*((3*(math.pi**2)*ne)**(2/3))
    
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
Fermie= fermirootfinder(-2,1,1,.001)

print(F"The Fermi energy is {Fermie}.")
