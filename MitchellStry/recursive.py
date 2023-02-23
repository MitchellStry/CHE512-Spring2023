import sys
def factorial(n):
    """
    Finds the factorial of a number input.
    """
    if (n<0):
        print('cannot define the factorial of a negitive number \n')
        sys.exit(0)
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1)*n

