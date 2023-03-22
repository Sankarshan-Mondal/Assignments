#Ans 1.a
x = []
for i in range(10):
	x.append(i)
print('x =', x)

#Ans 1.b

y = []
for i in range(3,13):
	y.append(i)
print('y =', y)

#Ans 1.c

print('The reverse order:', x[::-1])

#Ans 1.d

print(x[1:11:2], x[0:11:2])
print('the combined:', [i for i in x if i%2!=0], [i for i in x if i%2==0])

#Ans 1.e

print('The result is:', x[3]==y[0])

#Ans 1.f

if 10 in x:
	print('The index is:', x.index(10))
else:
	print('Not availabe')

#Ans 1.g

print('The location is:', x.index(7)+1)

#Ans 1.h

print('the list is', x+y)

#Ans 1.i

z = x+y

print('The location of maxima:', z.index(max(z))+1)
print('The location of minima:', z.index(min(z))+1)


#Ans 2.a
x = 'The quick brown fox jumps over the lazy dog'

#Ans 2.b
if 'fox' in x:
	print(f'The word fox is there in {x}')

#Ans 2.c
print('the sentence becomes:', x[::-1])

#Ans 2.d
print('Every third character:', x[::3])

#Ans 2.e
print('Every fourth character:', x[::4])

#Ans 2.f
print('the no. of characters', len(x))

#Ans 2.g
print('every 2nd character from the end:', x[::-2])

#Ans 2.h
y = x[0:4]
z = x[-1:-4:-1]
 z = z[::-1]

print('y+z =', y+z)

#Ans 2.i
print('y*10=', y*10)


