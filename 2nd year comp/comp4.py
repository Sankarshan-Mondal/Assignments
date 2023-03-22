#Ans 1

def f(x):
	return x**3 + x**2 - x

def df(x):
	return 3*x**2 + 2*x - 1

a=0
b=1


while abs(f(a))>0.0001:
	h =  f(a)/df(a)
	a-=h

print(a)

#Ans 1

L1 = [1,2,3,5,6,7]
L2 = [5,6,7,8,9,0]
L3=[i for i in L1 if i not in L2]
print(L3)

'''for i in L1:
	if i not in L2:
		L3.append(i)
print(L3)'''


#Ans 2
import math as m

r = float(input('radius:'))
h = float(input('height:'))

x = lambda r,h : m.pi*(r**2)*h

print('Volume:', x(r,h))

#Ans 3
name = str(input('Name:'))
B = float(input('basic salary:'))

DA = (17/100)*B
HRA = (8/100)*B
MA = (10/100)*B

T = DA+HRA+MA

#n = len(name)+2

print('The salary of %7s is %10.3f ruppes' %(name, T))


#Ans 4
import numpy as np

n = int(input('enter integer:'))

for i in range(1, n+1):
	for j in np.arange(1.0, i+0.5, 0.5):
		print(str(j), end=' ')
	print()

#Ans 5
def encrypt(asci):
	s = 'abcdefghijklmnopqrstuvwxyz'
	p = [s[25-s.index(i)] for i in asci]
	z = ''.join(p)
	#for i in asci:
		#s[25-s.index(i)]
	return z

print(encrypt('abc'))

#Ans 6
s = str(input('enter string:')
n = len(s)
m = n//2

if n%2==0:
	snew = s[m:n] + s[0:m]
else:
	snew = s[m+1:n] + s[m] + s[0:m]
	
print(snew)


#Ans 7
n=input('Enter integer:').split(',')

new=[]

for i in n:
	if n.count(i)==1:
		new.append(int(i))
print(new)

#slight mismatch left as 1 q missed






