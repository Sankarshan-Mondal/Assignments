#importing required packages
import math as m
import numpy as np

#Defining the given function
def f(x):
    return (m.log(x, m.e) + 0.5)

x = 0.1

a=0
b=1

while f(a)*f(b)<0:
    while f(a)*f((a+b)/2)<0:
        b=(a+b)/2
    while f(b)*f((a+b)/2)<0:
        a=(a+b)/2

while (b-a)**2<0.001:
    print(a)

