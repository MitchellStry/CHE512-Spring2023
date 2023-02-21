import math
#import cmath

def quadratic_func(A, B, C):
     """
     This function looks for the roots 
     of a quadratic equation of form
     A * x^2 + B * x + C = 0
    
     (-b +- sqrt(b^2 - 4 * a * c))/ (2*a)
     """
     root1 = (-B + math.sqrt(B**2 - 4 * A * C))/ (2*A)
     root2 = (-B - math.sqrt(B**2 - 4 * A * C))/ (2*A)
     return root1, root2

roots = quadratic_func(1, -11, 30)
print(roots)
