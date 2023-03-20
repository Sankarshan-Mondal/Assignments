#Ans 6.1
'''import numpy as np
a = np.array([[1,2,3],[4,8,66],[7,81,9]])
b = np.array([[2],[3],[4]])
if np.linalg.det(a)>0.0000001:
    c = np.linalg.solve(a,b)
print(c)'''

import numpy as np
a = np.array([[1,2,3],[4,8,66],[7,81,9]])
b = np.array([[2],[3],[4]])
print(a,'\n', b)
if abs(np.linalg.det(a))>0.0000001:
    x=np.linalg.solve(a,b)

print(x)

#Ans 6.2
#defining the binary converter
def d2b(n):
    s=[]
    while n>=1:
        s.append(n%2)
        n = n//2
    s = [str(i) for i in s]
    a = ''.join(s)
    a = a[::-1]
    a = int(a)
    return a

#defining function that acts on an array
def numpy_DecimalToBinary(A):
    for i in A:
        A[A==i] = d2b(i)
    return A

A = np.array([1,2,3,4,5])
print(numpy_DecimalToBinary(A))

#Ans 6.3.1 and Ans 6.3.2
import numpy as np
A = np.array([[50,60,70],[67,88,90],[60,78,97]])
print(A[0][0],A[1][0],A[2][0])


def sum_stud(i):
    s = []
    for j in range(3):
        s.append(A[j][i])
    return sum(s)


def sum_sub(i):
    s = []
    for j in range(3):
        s.append(A[i][j])
    return sum(s)

n = int(input('Enter a number:'))
print('The sum of scores of rank{} student:'.format(n), sum_stud(n))
print('The sum of scores of rank{} subject:'.format(n), sum_sub(n))


#Ans 6.4
A = np.array([1,2,3,4,5,6])
B = np.array([4,5,6,7,8,9])
C = []
for i in A:
    if i in B:
        C.append(i)
        A = np.delete(A, np.where(A==i))

C = np.array(C)
print(A)
print(B)
print(C)

#Ans 6.5
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[3,3],[1,1]])

print('first array:\n', arr1)
print('second array:\n', arr2)
print('elementwise multiplication:\n', np.multiply(arr1,arr2))
print('matrix multiplication:\n', np.matmul(arr1,arr2))

