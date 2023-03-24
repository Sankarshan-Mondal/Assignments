import numpy as np
import math as m

#part a.
#taking two random arrays to work on--
A = np.array([1,2,3,4,5]) 
B = np.array([6,7,8,9,0])

s=0 #setting an initial value 0 to the dot product
if len(A)==len(B): #checking the possibility of dot product
    for i in range(len(A)): #iterating the respectively indexed numbers
        b = A[i]*B[i]
        s+=b #adding each iteration to the value of s
print('A.B=', s) #obtaining the final dot product



#part b.

ab = 0 #initializing the dot product
a2 = 0 #initializing the variance of a
b2 = 0 #initializing the variance of b
if len(A)==len(B): #checking the possibility of dot product
    for i in range(len(A)): #iterating the values
        ab += A[i]*B[i] #adding each iteration to the initial value
        a2 += A[i]**2
        b2 += B[i]**2

        
cosAB = ab/(m.sqrt(a2)*m.sqrt(b2)) #applying te relation provided using math package

print('cos(A,B)=',cosAB) #output