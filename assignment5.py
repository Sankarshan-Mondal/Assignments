#CS1101
#Assignment 5_2021-batch

#Ans 1
n = int(input('The first integer: '))
o = int(input('The second integer: '))

print('The prime numbers lying between the numbers are: ')
if o > n:
    
    for i in range(n+1, o):
        if i > 1:
            for j in range(2, i):
                if (i%j) == 0 :
                    break
            else:
                print(i)
                
elif o < n:
    for i in range(o+1, n):
        if i > 1:
            for j in range(2, i):
                if (i%j) == 0 :
                    break
            else:
                print(i)
                
#Ans 2
import math

for n in range(1000):
    x = math.pi
    a = 1
    y = [1]
    #We are already taking the first term because without using factorial function, it is difficult to iterate 1 from the loop.
    for i in range(1,n+1):
        a = (x/i)*a
        y.append(a)
        
    if math.fabs(sum(y) - math.exp(math.pi)) <= 10**(-4):
        print('The number of terms in the series: ', n+1)
        break
    

print('The computed value: ', sum(y))
print('The original value: ', math.exp(math.pi))
print('The absolute difference between the values: ', float(math.fabs(sum(y) - math.exp(math.pi))))

#Ans 3
import math

b = []
for n in range(1000):
    x = float(math.pi/2)
    b.append((-1)**n*((x)**(2*n+1))/math.factorial(2*n+1))

    if math.fabs(sum(b) - math.sin(math.pi/2)) <= 10**(-4):
        print('The number of terms in the series: ', n+1)
        break

print('The computed value of sequence: ', sum(b))
print('The actual value of the sequence: ', math.sin(math.pi/2))
print('The absolute difference between the values: ', math.fabs(sum(b) - math.sin(math.pi/2)))

#Ans 4
x = 'A'
y = ' '

n = int(input('Enter any number to generate the triangle: '))
# Recommended number according to question is 10

for i in range(n+1):
    print((n-i)*y + 2*i*x + (n-i)*y)
    
#Ans 5
x = float(input('enter first length: '))
y = float(input('enter second length: '))
z = float(input('enter third length: '))

s = [x, y, z]
s.sort()

print('The sides are capable of forming a Triangle: ')

if (s[0] + s[1]) > s[2]:
    print('True')
else:
    print('False')
    
#Ans 6
#I have defined f(x, n) in the second part of the answer.
import math
for j in range(5000):
    x = 1
    
    b = 0
    for i in range(j+1):
        a = ((-1)**(i)*x**(2*i+1))/(2*i+1)
        b += a
    if math.fabs(math.pi - 4*b) <= 10**(-3):
        print('The minimum number of terms required to compute pi: ', j)
        break

def f(x,n):
    n = int(input('Input the obtained number to get pi according to accuracy: '))

    x = 1
    
    b = 0
    for i in range(n+1):
        a = ((-1)**(i)*x**(2*i+1))/(2*i+1)
        b += a
        
    return(b)

pi_form = 4*f(5,1)
pi_org = math.pi        
print('The value of pi is: ', pi_form)
print('The original value of pi: ', pi_org)

print('The difference between actual and computed result: ', math.fabs(pi_org - pi_form))


#Ans 7
def f(x):
    return x**(9/10)

itt = []

x = 10

while f(x) >= 2:
    itt.append(f(x))
    x = f(x)
itt.append(f(x))

print('The list of all the iterations upto x<2: ', itt)
print('The number of iterations required: ', len(itt))
