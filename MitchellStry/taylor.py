import math
def taylor1(taylor_aporx,exact):
    """"
    This function should compute 1/(1-x) using taylor series epansions 1/(1-x) aprox 1+x+x^2+x^3...
    conditions 0<x<1
    returns:
    tuple:taylor_apporx, exact result
    """
    #I did update this in class, originally being the file named as the date of the class we did taylor stuff
    x=taylor_aporx
    N=exact
    taylor,exact=0.0,1.0/(1-x)
    exact_value=math.exp(x)
    print(f'The exact value of e^{x}={exact_value}')

    n=0
    x1=0
    while n<N:
        x1=x1+(x**n)
        n+=1

    print(f'The aproximate vale is {x1}')
    taylor=x1
    return taylor, exact
print('_______________________________________________________________________________')
print(f'The first number is the exact value and the second is the taylor aproximation {taylor1}')

