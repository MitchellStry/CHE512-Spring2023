import math

def f1(x):
    return x

def f2(x):
    return x**2

def f3(x):
    return math.sin(x)



def der_estimate(f, x, dx):
    dfdx = (f(x+dx) - f(x-dx))/(2.0*dx)
    return dfdx


def derivative(f, x, eps):
    # Initialize dx - whatever the value
    dx = 1.0

    err = 2.0 * eps
    it = 1

    while err > eps:
    
        dfdx1 = der_estimate(f, x, dx)

        # Now, compute all the above at x+dx/2 and x-dx/2
        dfdx2 = der_estimate(f, x, dx/2)

        # Compare the absolute difference of the two values 
        err = abs(dfdx1 - dfdx2)

        print(F"iteration number = {it} derivative = {dfdx2} error = {err}")

        dx = dx / 10.0
        it = it + 1


derivative(f1, 0.0, 1e-20)   


derivative(f2, 0.0, 1e-20)

derivative(f2, 1.0, 1e-20)

derivative(f2, 10.0, 1e-20)


derivative(f3, 1.0, 1e-80)
print(F"exact derivative = { math.cos(1) }")
