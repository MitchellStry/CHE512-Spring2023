import cmath

def sqroots(a,b,c):
    """
    This function computes the square roots of the a*x^2+b*x+c=0 equation.
    """
    delta = cmath.sqrt((b**2-4*a*c))
    x1 = (-b+delta)/(2*a)
    x2 = (-b-delta)/(2*a)
    return x1, x2

print(sqroots(10, 3, -1.5))

def taylor_series1(x, n):
    """
    This function comptues the 1/(1-x) using Taylor series expansion
    """
    taylor = 0.0
    exact = 1/(1-x)
    y = 1.0
    for i in range(n):
        taylor += y
        y *= x
 
    return taylor, exact

print(taylor_series1(0.5, 100))

def taylor_series2(x, n):
    """
    This function comptues the sin(x) using Taylor series expansion
    """
    taylor = 0.0
    exact = cmath.sin(x)
    c = 1
    x2 = x**2
    for i in range(1,n):
        taylor += c*x
        c /= ((2*i+1)*(2*i))
        x *= x2
        c *= -1
 
    return taylor, exact

print(taylor_series2(cmath.pi, 100))


