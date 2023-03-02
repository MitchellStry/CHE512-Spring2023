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
def taylor_series(x, n):
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

print(taylor_series(10, 100))
#def 
