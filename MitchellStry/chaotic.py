import math

def series(x0,r,n):
    ist=[]
    xn=x0
    for i in range(n):
        ist.append(xn)
        xn=4*r*xn*(1-xn)
    return ist
print(series(0.3,0.8,25))
