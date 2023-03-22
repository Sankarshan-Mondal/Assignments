#CS1101
#Assignment 6_2021 batch

#Ans 1
def g(n):
    s = []
    for i in range(1,n+1):
        s.append(i/(i+1))
    return sum(s)

for n in range(1, 21):
    print('The value of g(n) for n =', n, 'is: ', g(n))
    
#Ans 2
import math

def f(n):
    s = []
    for x in range(1,n+1):
        s.append(x)
    return(math.prod(s))

for n in range(1,9):
    print('The factorial of', n,'is: ', f(n))
    
#Ans 3
from math import *

def f(t):
    return sin(2*t*pi/180)

for x in range(10):
    print('The angles and the outputs are: Ɵ =', 10*x, 'and sin(2Ɵ) =', f(10*x))
    
#Ans 4
#the code with known input
a = 'Satyajit Ray'
print('Input: Enter a text: ', a)
a = list(a)

for x in range(len(a)):
    if x%2==0:
        a[x],a[x+1] = a[x+1],a[x]

a = ''.join(a)
print('Output: The result is: ', a)

b = 'Covid19 Vaccine'
print('Input: Enter a text: ', b)
b = list(b)

for x in range(len(b)-1):
    if x%2==0:
        b[x],b[x+1] = b[x+1],b[x]

a = ''.join(b)
print('Output: The result is: ', a)

#the code with unknown input
a = input('Enter a text: ')
if len(a)%2==0:
    a = list(a)

    for x in range(len(a)):
        if x%2==0:
            a[x],a[x+1] = a[x+1],a[x]

    a = ''.join(a)
    print('The result is:', a)

else:
    a = list(a)

    for x in range(len(a)-1):
        if x%2==0:
            a[x],a[x+1] = a[x+1],a[x]

    a = ''.join(a)
    print('The result is:', a)
    
    
#Ans 5
#The code with the given sentence
s = 'Indian Statistical Institute (ISI) is a public research university.'
t = s[::-1]

j = s.find('(')
k = t.find(')')

print('Input: ', s)
s  = s[0:j:] + s[len(s)-k::]
print('Output: ', s)

#The code with required input
s = str(input('Enter a text (with brackets): '))
t = s[::-1]

j = s.find('(')
k = t.find(')')

s  = s[0:j:] + s[len(s)-k::]
print('Output: ', s)


#Ans 6
s = []

j = int(input('Enter an integer: '))

for i in range(1,j+1):
    print('Enter value', i,':')
    k = int(input())
    s.append(k)

p = []
q = []
for i in s:
    if i%2 == 0:
        p.append(i)
    else:
        q.append(i)
        
print('Output: ')
print('Number of even numbers: ', len(p))
print('Number of odd numbers: ', len(q))


#Ans 7
def f(n):
    s = []
    for x in range(1, n+1):
        s.append(int(x*'3'))
    return sum(s)

#The code with provided input
print('Enter an integer: 6')
print('The result is: ', f(6))

print('Enter an integer: 9')
print('The result is: ', f(9))

#The code which requires input
n = int(input('Enter an integer: '))
print('The result is: ', f(n))

#Ans 8
import math
print('The strong numbers between 1 and 100000 are: ')
for x in range(1,100000):
    y = str(x)
    y = list(y)
    s = []
    for i in range(len(y)):
        z = int(y[i])
        s.append(math.factorial(z))
        if  x == sum(s):
            print(x)
            
#Ans 9
p = (1900*365) + (1900//4) + 1


y = int(input('Enter year: '))
m = int(input('Enter month: '))
d = int(input('Enter date: '))

print('The day was: ')

if y%4 == 0:
    month = [0,31,29,31,30,31,30,31,31,30,31,30]

    q=0
    for i in range(m):
        q += month[i]

    if (y*365 + (y//4) -1 + q + d - p)%7 == 0:
            print('monday')
    elif (y*365 + (y//4) -1 + q + d - p)%7 == 1:
            print('tuesday')
    elif (y*365 + (y//4) -1 + q + d - p)%7 == 2:
            print('wednesday')
    elif (y*365 + (y//4) -1 + q + d - p)%7 == 3:
             print('thursday')
    elif (y*365 + (y//4) -1 + q + d - p)%7 == 4:
             print('friday')
    elif (y*365 + (y//4) -1 + q + d - p)%7 == 5:
            print('saturday')
    elif (y*365 + (y//4) -1 + q + d - p)%7 == 6:
             print('sunday')

else:
    month = [0,31,28,31,30,31,30,31,31,30,31,30]

    q=0
    for i in range(m):
        q += month[i]    
    if (y*365 + (y//4) + q + d - p)%7 == 0:
            print('monday')
    elif (y*365 + (y//4) + q + d - p)%7 == 1:
            print('tuesday')
    elif (y*365 + (y//4) + q + d - p)%7 == 2:
            print('wednesday')
    elif (y*365 + (y//4) + q + d - p)%7 == 3:
             print('thursday')
    elif (y*365 + (y//4) + q + d - p)%7 == 4:
             print('friday')
    elif (y*365 + (y//4) + q + d - p)%7 == 5:
            print('saturday')
    elif (y*365 + (y//4) + q + d - p)%7 == 6:
             print('sunday')


    

