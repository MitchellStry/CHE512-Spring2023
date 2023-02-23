import cmath, math, sys
#import cmath


def quadratic_func(A, B, C):
     """
     This function looks for the roots 
     of a quadratic equation of form
     A * x^2 + B * x + C = 0
    
     (-b +- sqrt(b^2 - 4 * a * c))/ (2*a)
     """

     det = B**2 - 4 * A * C

     if det>=0.0:
         #print("Positive determinant, all good\n")
         sq = math.sqrt(B**2 - 4 * A * C)

         denom = (0.5/A)
         root1 = (-B + sq) * denom
         root2 = (-B - sq) * denom

     else:         
         print("Determinant is negative. Exiting...\n")
         sys.exit(0)


     return root1, root2


a = -1.0   # simulation time
b = 1.0   # integration timestep
c = 30.0


roots = quadratic_func(a, b, c)
print(roots)



