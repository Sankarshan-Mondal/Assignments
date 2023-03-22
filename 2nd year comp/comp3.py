#Set 3

#Ans 1.
L = [1,3,5,7]
L.insert(L.index(1)+1, 2)
L.insert(L.index(3)+1, 4)
L.insert(L.index(5)+1, 6)
print(L)

#Ans 2.
L.pop()
print(L)

#Ans 3.
L=[]
def Push(L, e):
    return L.append(e)

Push(L,1)
Push(L,2)
Push(L,3)
Push(L,4)
Push(L,5)
print('L from Push command', L)

#Ans 4.

def Pop(L):
    x = L[len(L)-1]    
    L.pop()
    return x

print(Pop(L))
print('L with last element removed:', L)


#Ans 5.
L=[]
Push(L, 'name1')
Push(L, 'name2')
Push(L, 'name3')
Push(L, 'name4')
Push(L, 'name5')

print(L)

print('The required order is:')
while len(L)>0:
    print(Pop(L))



#Ans 6.
a = str(input('Enter a string:'))
L = list(a)
#print(L)
S=[]
while len(L)>0:
    S.append(Pop(L))  
b= ''.join(S)
#print(b)

if a==b:
    print('the string is a palindrome')
else:
    print('the string is not a palindrome')
   
#Ans 7.
   
L = [1,3,3,3,3,3,3,3,3,3,3,3,3,5,6,66,6,7]
for i in L:
    while L.count(i)>1:
        L.remove(i)
print(L)


#Ans 8.
L = [1,2,3,4,5]
L1 = []
for i in L:
    if i%2==0:
        L1.append(i)
print(L1)


#Ans 9.
L1 = [1,2,3,4,5]
L2 = [5,4,10,12]

L3 = []
m=0
n=0
for i in L1:
    if i%2==1:
        m+=i
L3.append(m)
for i in L2:
    if i%2==1:
        n+=i
L3.append(n)
print(L3)

#other solution
L3=[]
for i in L1:
    if i%2!=0:
        for j in L2:
            if j%2!=0:
                L3.append(i+j)
               
print(L3)


#Ans 10.
n = int(input('Enter an even number:'))
while n%2!=0:
    print('Try again')
    n = int(input('Enter an even number:'))
print('thank you')


#Ans 11.
n = int(input('enter an integer:'))
a = 0
j=0
i=0

while n/10**j>1:
    print(j)
    j+=1
print(j)

while i<j:
    b=n%10
    a+=b*(10**(j-i-1))
    n = n - b
    n=n/10
    i+=1

a=int(a)

print('The reverse number is:', a)


#Ans 12.
d = {1 : 'ONE', 2 : 'TWO', 3 : 'THREE', 4 : 'FOUR', 5 : 'FIVE', 6 : 'SIX', 7 : 'SEVEN', 8 : 'EIGHT', 9 : 'NINE'} 

n=int(input('enter your integer:'))

for i in str(n):
	print(d[int(i)], end=' ')
print()


#Ans 13.
import math as m




def f(x):
	return m.sin(x)+x**2-1

l = 0
u = 1
k = 0.01

while f(l)*f(l+k)>0:
	l += k
print(l,l+k,f(l))

a=l
b=l+k
#mid = (a+b)/2
#print(mid)


while b-a>0.00001:
	if f(a)*f((a+b)/2)<0:
		b = (a+b)/2
		#print(b)
	if f((a+b)/2)*f(b)<0:
		a = (a+b)/2
		#print(a)
#if (b-a)<0.1:
print(a, f(a))


#Ans 14















