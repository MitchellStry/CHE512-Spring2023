import math

def f1(x):
    return x

def f2(x):
    return x**2

def f3(x):
    return math.sin(x)

def dfest(f,x,dx):
    dfdx=(f(x+dx)-f(x-dx))/(2*dx)
    return dfdx

def der(f,x,eps):
    dx=1.0
    err= eps*2
    it=0
    while err>eps:
        it=it+1
        dfdx1=dfest(f,x,dx)
        dfdx2=dfest(f,x,dx/2)
        err=abs(dfdx1-dfdx2)
        print(F"iteration number = {it} derivitive {dfdx2} error={err}")
        dx=dx/10

der(f2,0.0,1e-20)

der(f2,0.1,1e-20)

der(f2,1.0,1e-20)

der(f2,10.0,1e-20)

der(f3,1.0,1e-80)
print(F"exact derivitive is {math.cos(1)}")
