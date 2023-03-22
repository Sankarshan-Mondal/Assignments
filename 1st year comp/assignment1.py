#CS1101 Assignment01
#Q1)Exploring lists

#Ans 1b
x = list(range(11))

#Ans 1c
y = list(range(3,13))

#Ans 1d
z = x[-1:-11:-1]
print(z)

x = list(range(10))

#Ans 1e
odd_nos = [num for num in x if num % 2 == 1]
print("Odd numbers in the list: ", odd_nos)

even_nos = [num for num in x if num % 2 == 0]
print("Even numbers in the list: ", even_nos)


#Ans 1f
print(x[3])
print(y[0])
if x[3] == y[0]:
    print('true')
else:
    print('false')

#Ans 1g
print(10 in x)

#Ans 1h
print(7 in y)

#Ans 1i
print(x+y)

#Ans 1j
    #part 1
x = x[-1:-11:-1]
z = x + y
print(z)
    #part 2
print(z.index(max(z)))
print(z.index(min(z)))



#Q2)Strings and lists

#Ans 2a
x = "The quick brown fox jumps over the lazy dog"

#Ans 2b
print('fox' in x)
print(x.find('fox'))

#Ans 2c
print(len(x)) #finding the length of the string is helpful in reversing it.
p = list(x)
print(p)
rev = p[-1:-44:-1]
print(rev)

newstr = ''.join(rev)
print(newstr)


#Ans 2d
l=len(x)
for i in range(2,l,3):
    print(x[i])

#Ans 2e
l=len(x)
for j in range(3,l,4):
    print(x[j])

#Ans 2f
print(len(x))

#Ans 2g
l=len(x)
for i in range(-1,-(l+1),-2):
    print(x[i])
    
#Ans 2h
y = x[0:4:1]
z = x[40:44:1]

print(y+z)

#Ans 2i
print(y*10)


#Q3) Numbers

#Ans 3a
x = 1.2

#Ans 3b
y = 12

#Ans 3c
z = 24

#Ans 3d
print(x/y)
print(y/z)
print(z/x)
#Yes, All of them are floats.

#Ans 3e
print(3**7)

#Ans 3f
if 2.0**3 == 8.0:
    print('True')
else:
    print('False')

#Ans 3g
print(y+z)
print(str(y)+str(z))

#Q4) Miscellaneous

#Ans 4a and 4b
print('Hello World') #This is my comment on this program : 'Hello world is printed on the console'

#Ans 4c
name = 'Tintin'
age = 20
roll = '21MS1234'

print('Name: ', name)
print('Age: ', age)
print('Roll Number: ', roll)

print('Hello! My name is ',name,'. I am ', age, ' years old. My roll number is ', roll, '.', sep='')

#Ans 4d
a = '1357'
b = '2468'
print(a+b)

#Ans 4e
c = 1357
d = 2468
print(c+d)

#Ans 4f
print("It's good to learn Python")

#Ans 4g
print('The man asked, "Where to meet you?" I said, "Well, use Google Meet!"')

#Ans 4h
print(type(c)) #c variable is used in answer 4e

#Ans 4i
Name = 'Sankarshan'
print('My name is', Name)

#Ans 4j
nm = 'Sherlok'
ag = 40
gender = 'Male'

print("Good Morning ", nm,"! You are a ", gender," of ", ag," years.", sep='')

