#importing required packages
import math as m
import numpy as np

#Defining the given function
def f(x):
    return m.log(x, m.e) + 0.5


a=0.1
b=1

i = 0 #for counting the number of iterations
while f(b) > 0.00001: #we are choosing accuracy to be 0.00001
    b = b - (f(b)*(b-a))/(f(b)-f(a))

    
    i += 1 #counting the number of iterations
    #print(b) gives us the iterative value at each step

print('The root of the function:', b) #the root
print('The number of iterations:', i) #number of iterations



