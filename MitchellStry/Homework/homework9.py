import math

def f1(x):
    return x

def f2(x):
    return x**2

def f3(x):
    return math.sin(x)


def integ(a,b,c,eps):
    n=1
    err=eps*2
    inte1=traprule(a,b,c,n)
    while err>eps:
        n=n*2
        inte2=traprule(a,b,c,n)
        err=abs(inte2-inte1)/3
        print(F"This is interation {n} integral is {inte2} and error is {err}")
        inte1=inte2

def traprule(a,b,c,n):
    dx=(c-b)/n
    x=b
    integ=0
    for i in range(n):
        integ= integ+(a(x)+a(x+dx))*dx/2
        x=x+dx
    return integ





integ(f2,-2.0,2.0,1e-20)
integ(f3,-1.0,1.0,1e-80)
