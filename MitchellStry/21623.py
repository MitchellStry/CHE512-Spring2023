def sqreets(a,b,c):
        """"
         This function looks for roots of a quadratic equation
         Ax^2 + Bx + C = 0
         ((-b +/- sqrt(b^2-4*a*c)/(2*a))
         Returns:tuple (root1,root2)
         """
         a=int(a)
         b=int(b)
         c=int(c)
         root1=(-b + cmath.sqrt(b**2-4*a*c))/(2*a)
         root2=(-b - cmath.sqrt(b**2-4*a*c))/(2*a)
         print(root1, root2)
         return root1, root2
         r1,r2=sqreets(1,2,3)
