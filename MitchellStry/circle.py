import math
import random
import numpy as np

for i in range(10):
    print(random.uniform(0,1))

def compute(N):
    x=np.random.uniform(-1,1,100)
    y=np.random.uniform(-1,1,100)
    counter=0
    for i in range (N):
        dist=x[i]**2 + y[i]**2
        if dist<1.0:
            counter=counter+1
    prob=counter/N
    res=4*prob
    return res,np.py
#print(x)

