#importing required packages
import math as m
import numpy as np

#Defining the given function
def f(x):
    return m.log(x, m.e) + 0.5


a=0.1
b=1

i = 0 #for counting the number of iterations
while f(b) > 0.001:
    b = b - (f(b)*(b-a))/(f(b)-f(a))

    
    i += 1 #counting the number of iterations

print(b) #the root
print(i) #number of iterations



