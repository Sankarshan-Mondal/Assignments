#CS1101_Assignment_3_2021


#Ans 1

n = int(input('Enter your number here, i = '))

total = 0

for x in range(1, n+1):
    total += x**2

print('The claculated sum of i squares is: ', total)

n = int(input('Enter your number here, i = '))

total = 0

for x in range(1, n+1):
    total += x**3

print('The claculated sum of i cubes is: ', total)

n = int(input('Enter your number n here: '))

print('The sum of suares of the numbers using the formula is: ', n*(n+1)*(2*n + 1)/6)

n = int(input('Enter your number n here: '))

print('The sum of cubes of the numbers using the formula is: ', (n**2)*((n+1)**2)/4)


#Ans 2

n = int(input('The number of odd numbers in the list: '))

k = []

for x in range(1, 2*n+1, 2):
    k.append(x)
    k.append(0)
k.pop()    
print(k)


#Ans 3

n = int(input('number of terms in the list: '))

j = []

for x in range(1,n+1):
    j.append(x**2)
    
print(j)

#Ans 4

n = int(input('Enter the "n" for which you want to calculate the pattern: '))

x = 1

for m in range(1, n+1):
    x = 1 + m/x
    
print(x)
    

#Ans 5

n = int(input('Type the number of Fibonacci numbers you need: '))

x = 1
y = 0

for z in range(n):    
    z = x + y
    x = y
    y = z
    print(z) 
    

#Ans 6
while True:
    n = float(input('Enter the Number whose square root you want to find : '))
    
    if n >= 0:
        print('The square root is = ', n**(1/2))
        break
    print('Error!, Invalid input, try again')
    

#Ans 7.1
n = input('Enter a name: ')
k = int(input('Enter his/her age: '))

x = (n, k)

print('the touple: ', x)

#Ans 7.2
a = ('Raju', 18)
b = ('Shyam', 20)
c = ('Raghav', 22)
d = ('Aman', 21)
e = ('Raghu', 19)
f = ('Rajeev', 23)
g = ('Kartik', 22)
h = ('Kirti', 20)
i = ('Rajesh', 20)
j = ('Rakesh', 18)


n = [a,b,c,d,e,f,g,h,i,j]

print('The list of name and age is: ',n)

#Ans 7.3

x = str(input('Enter the name of the name of the student : '))
for y in n:
    if x in y:
        y = list(y)
        print('The age of the student is: ', y[1])

#Ans 8
n = str(input('Enter your mobile number: '))
x = ['0','1','2','3','4','5','6','7','8','9']
    
for y in x:
    if y not in n:
        print(y)
        

#Ans 9
rollnos = []


for x in range(1, 10):
    rollnos.insert(x-1 , ('20MS00' + str(x)))
for x in range(10, 100):
    rollnos.insert(x-1 , ('20MS0' + str(x)))
for x in range(100, 251):
    rollnos.insert(x-1 , ('20MS' + str(x)))

#print(rollnos)

GroupA = []
GroupB = []

for x in range(250):
    if x < 150:
        GroupA.append(rollnos[x])
    else :
        GroupB.append(rollnos[x])
print('GroupA = ', GroupA)
print('GroupB = ', GroupB)



#Ans 10
farenheit = [10, 20, 30, 40, 50]
celsius = []

for n in range(5):
    celsius.append(5*(farenheit[n] - 32)/9)
    
print(celsius)


#Ans 11
marks = (54, 65, 48, 44, 88)
print('The original marks for CS1101, CH2201, CS3201, CS3202 and LS2201: ', marks)
mark = list(marks)

for x in range(len(mark)):
    if mark[x] < 50:
       mark[x] += 5
       
marks = tuple(mark)
       
print('The updated marks tuple is: ', marks)

    

