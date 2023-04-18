import math

def series(x0,r,n,name):
    name=str(name)
    with open(f"{name}.txt","w") as file:
        ist=[]
        xn=x0
        for i in range(n):
            ist.append(xn)
            xn=4*r*xn*(1-xn)
        xn=str(xn)
        file.write(f"The answeris {xn}")
        return ist



print(series(0.3,0.6,25,"six"))
print(series(0.3,0.7,25,"seven"))
print(series(0.3,0.8,25,"eight"))
