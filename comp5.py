#Ans 1

import numpy as np

x = np.array([[[1,2,3,4],[4,5,6,7]],[[6,7,8,9],[5,6,7,8]]])
print(x[0,:,0:3])

#Ans 2

import math as m
def calc_area(r):
	return m.pi*(r**2)

n = input('Enter radii: ').split(' ')

radius_list = []
for i in n:
	radius_list.append(int(i))

area_np = []

for i in radius_list:
	area_np.append(calc_area(i))


print('The respective radius and volume are:', radius_list, area_np)

#Ans 3

n = input('Enter radii: ').split(' ')

radius_list = []
for i in n:
	radius_list.append(int(i))

radius_list = np.array(radius_list)

area_np = calc_area(radius_list)

print('The respective radius and volume are:', radius_list, area_np)


#Ans 4
n = input('Enter name and age: ').split(' ')
d = {}
for i in n:
	if n.index(i)<len(n):
		if n.index(i)%2==0:
			d[i] = n[n.index(i)+1]
print(d)

#Ans 5
n = input('number:')
p = input('courses:')
d = {}
for i in range(int(n)):
    a = input('Name:')
    s=[]
    for j in range(int(p)):
        b = float(input('marks:'))
        s.append(b)
    s = np.array(s)
    d.update({a:s})
    print(s)
print(d)

#Ans 6
d_sum = {}
for i in range(int(n)):
    a = input('Name:')
    s=[]
    for j in range(int(p)):
        b = float(input('marks:'))
        s.append(b)
    s = np.array(s)
    d_sum.update({a:np.sum(s)})
    print(sum(s))
print(d_sum)


#Ans 7
a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6])

for i in range(len(a)):
    if a[i] == b[i]:
        print(True)
    else:
        print(False)
print(' ')
np.array_equal(a,b)
	







