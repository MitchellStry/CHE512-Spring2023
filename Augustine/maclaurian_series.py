import math

print("This programme computes the exact value for e^x \
and the approximate value using the Maclaurian series")

print('____________________________________________________')

x = float(input('Please enter the value of x: '))

print("The number of terms for the Maclaurian expansion should be a positive integer")
number_of_terms = int(input("Please enter number of peferred terms: "))


print('____________________________________________________')


def exponential_series(x):
    exact_value = pow(math.e, x) #This the exzct value function when you take exp(x)
    
    print(f'The exact value for e^{x} = {exact_value}')

    term = 1
    mac_series = 1
    terms = [1]
    while term < number_of_terms:
        mac_series += (pow(x, term)) / (math.factorial(term))
        term += 1
        current_term =  (pow(x, term)) / (math.factorial(term))
        terms.append(current_term)
    print('____________________________________________________')

    print(f'The sum of the terms: {terms} is {mac_series}')
    return exact_value , mac_series
    
result = exponential_series(x)
print('____________________________________________________')
print (f'The first number is the exact value and the second is the mac_series approximation {result}')


