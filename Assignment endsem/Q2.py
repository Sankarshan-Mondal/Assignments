import numpy as np
import math as m

#part a.
A = np.array([1,2,3,4,5])
B = np.array([6,7,8,9,0])

s=0
if len(A)==len(B):
    for i in range(len(A)):
        b = A[i]*B[i]
        s+=b
print(s)



#part b.

ab = 0
a2 = 0
b2 = 0
if np.size(A)==np.size(B):
    for i in range(np.size(A)):
        ab += A[i]*B[i]
        a2 += A[i]**2
        b2 += B[i]**2

        
cosAB = ab/(m.sqrt(a2)*m.sqrt(b2))

print(cosAB)