#Ans 2.1
x = 'abcdefghijkl'
for i in range(len(x)):
	print(x[i:])
	
#Ans 2.2
x = [12, 24, 56, 87, 54, 85, 100, 34, 76]

a=x[0]
for i in x:
	if i>=a:
		a=i
print('The max command is:', a)


#Ans 2.3
x = input('Enter your full name:')
z=[]
y = x.split(' ')
for i in range(len(y)):
	z.append(y[i][0])

print('The short form is:', '.'.join(z))

#Ans 2.4
a=1
b=1
print('The fibonnaci series is:')
for i in range(10):
	print(a)
	print(b)
	a=a+b
	b=a+b
	
#Ans 2.5
n = int(input('Enter number of your choice:'))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j, end=' ')
	print()
	
#Ans 2.6
n= int(input('No of numbers you need is:'))
for i in range(1,n+1):
	for j in range(i):
		print(2*j+1, end=' ')
	print()

#Ans 2.7
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end = ' ')
    print()

#Ans 2.8
s=[]
for i in range(1,6):
    s.append(str(i))
for i in range(4,0,-1):
    s.append(str(i))
#print(s)

s="".join(s)
for i in s:
    print(s)
    s=s.replace(i, ' ')
    
    
#Ans 2.9.1
d = {'one':'ones', 'two':'twos', 'three':'threes', 'four':'four'}

i = input('Enter user id:')
if i in d:
	p = input('Enter password:')
	if p == d[i]:
		print('Welcome to Portal!')
	else:
		print('Incorrect credentials')
else:
	print('Incorrect credentials')
	
#Ans 2.9.2
i = input('Enter user id:')
if i in d:
	z = input('Do you want password change? [y/n]')
	if z == 'y':
		p = input('Enter new password:')
		q = input('Enter new password:')
		if p==q:
			if d[i] != q:
				d[i]=q
				print('Credentials updated')
		else:
			print('Invalid credentials')
else:
	print('Invalid credentials')

print(d)


#Ans 2.10
import math as m


def f(x):
    return m.sin(x) + x**2 - 1

a=0
b=1

while f(a)*f(b)<0:
    while f(a)*f((a+b)/2)<0:
        b=(a+b)/2
    while f(b)*f((a+b)/2)<0:
        a=(a+b)/2

while (b-a)**2<0.001:
    print(a)









		
