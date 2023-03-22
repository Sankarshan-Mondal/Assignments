#Ans 7.1
import matplotlib.pyplot as plt
import numpy as np

a = int(input("Number of months:"))
d = {}
for i in range(a):
    x = int(input('Enter month:'))
    d[x] = float(input('Enter Rainfall:'))
dlist = list(d.keys())
dlist.sort()
sort_d = {i:d[i] for i in dlist}
x = np.array(list(sort_d.keys()))
y = np.array(list(sort_d.values()))

plt.plot(x,y)
plt.show()


#Ans 7.2

#Simple method
'''x = input('Enter month:').split(' ')
y = input('Enter rainfall in order with spaces:').split(' ')
z = input('Enter temperature in order with spaces:').split(' ')

plt.plot(x,z,y)
plt.scatter(x,y)
plt.scatter(x,z)'''


b = int(input("Number of months:"))
d = {}
t = {}
for i in range(b):
    x = int(input('Enter month:'))
    d[x] = float(input('Enter Rainfall:'))
    t[x] = float(input('Temperature:'))
dlist = list(d.keys())
dlist.sort()
sort_d = {i:d[i] for i in dlist}

dlist = list(t.keys())
dlist.sort()
sort_t = {i:t[i] for i in dlist}

x = np.array(list(sort_d.keys()))
y = np.array(list(sort_d.values()))
z = np.array(list(sort_t.values()))


plt.plot(x,z,y)
plt.scatter(x,y)
plt.scatter(x,z)
plt.show()

#Ans 7.3


#Ans 7.4

"""x = input('Enter montgh:').split(' ')
y = input('Enter rainfall').split(' ')
z = input('Enter temperature in spaces:').split(' ')

x = np.array(x)
y = np.array(y)
z = np.array(z)"""

plt.subplot(1,2,1)
plt.plot(x,y)
plt.xlabel('Months')
plt.ylabel('Rainfall')

plt.subplot(1,2,2)
plt.plot(x,z)
plt.xlabel('Months')
plt.ylabel('Temperature')


plt.show()

plt.subplot(2,1,1)
plt.plot(x,y)
plt.xlabel('Months')
plt.ylabel('Rainfall')

plt.subplot(2,1,2)
plt.plot(x,z)
plt.xlabel('Months')
plt.ylabel('Temperature')

plt.show()


#Ans 7.5
plt.bar(x,y,z)
plt.title('Bar Graph')
plt.xlabel('Months')
plt.ylabel('Rainfall')
plt.show()

#Ans 7.6
plt.bar(x,z)
plt.title('Bar Graph')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()

#Stylish bar
plt.bar(x - 0.2, y, 0.4)
plt.bar(x + 0.2, z, 0.4)
plt.title('Bar Graph')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()

#Ans 7.7
plt.pie(x)
plt.title('Variation in rainfall')
plt.show()

#Ans 7.8
import random as r
n = int(input('Number:'))

d = {}
s = []
for i in range(1,n+1):
    x = r.random()
    if x<0.5:
        s.append(x)
    d[i]= len(s)/i
x = np.array(list(d.keys()))
y = np.array(list(d.values()))

plt.plot(x,y)
plt.xlabel('Number of tosses')
plt.ylabel('Net probability')
plt.show()

