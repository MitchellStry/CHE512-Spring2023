import cmath, math, sys
def qreets(a,b,c):
    """"
    This function looks for roots of a quadratic equation Ax^2 + Bx + C = 0 and Returns:tuple (root1,root2)
    """
    #I Did edit this in class, updating from the file named as the date of the class we made the original square root function.
    a=float(a)
    b=float(b)
    c=float(c)
    det=(b**2 - 4*a*c)
    if det >= 0.0:
        print("positive determinant. all good \n")
        sq=cmath.sqrt(b**2 - 4*a*c)
        denom=(0.5/a)
        root1=(-b + sq) *denom
        root2=(-b - sq) *denom
    else:
        print("determinant is negitive. Exiting \n")
        sys.exit(0)
   return root1, root2
print(root1,root2)
