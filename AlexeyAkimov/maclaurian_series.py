import math




def exponential_series(x, N):
    exact_value = math.exp(x)        
    print(f'The exact value for e^{x} = {exact_value}')


    n = 0
    mac_series = 0.0
    x_to_n = 1.0
    fact_n = 1.0

    while n < N: 
        mac_series += x_to_n / fact_n
        x_to_n *= x
        fact_n *= (n + 1.0)       
        n += 1

    print(f'The approximate value is {mac_series}')
    
    

exponential_series(1.0, 10)

