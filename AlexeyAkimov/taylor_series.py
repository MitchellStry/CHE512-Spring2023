#import math

#This programme computes exact value for 1 / (1 - x) and the approximate value using Taylor's approximation 

print('This programme computes exact and approximate value for 1 / (1 - 0.4)')
print('The approximation only use four terms for the expansion')

def taylors_series(x):
    exact_value = 1 / (1 - x) #Function to calculate the exact value

    '''
    The taylor expansion for 1 / (1 - x) for small values of x less than one is in
    the form 1 + x + x^2 + x^3 + ... + x^n
    '''
    i = 1
    taylor_approximation = 1
    end = 4 # Number of terms for approximation
    number_of_terms = end
    while i <= number_of_terms:   #Loop that generates the terms for the expansion
        taylor_approximation = taylor_approximation + pow(x, i)
        i += 1    
    
    return exact_value , taylor_approximation

values = taylors_series(0.4)
print (f' The first number in the tuple below is the exact value and the second is the taylors approximation.')
print(values)

