#CS1101_Assignment 4_2021-batch

#Ans 1

matrix = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

output = []

for sublist in matrix:
   if type(sublist) == list:
        for x in sublist:
            output.append(x)
for y in matrix:
    if type(y) == int:
        output.append(y)
    
output.sort()

print('The original list was: ', matrix)       
print("The new list formed is: ", output)

#Ans 2
print('Input: ')
r = int(input('Enter no. of Rows: '))
c = int(input('Enter no. of Columns: '))

matrix = []

for x in range(1, r+1):
    a = []
    for y in range(1, c+1):
        print('Enter element at Row: ', x, ', Column: ', y,': ')
        a.append(int(input()))
    matrix.append(a)

print('Output--')
print('The required matrix is: ')
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = ' ')
    print()

#Ans 3
x = [3,7,13,9,7,5,13,17,23,17,7,29]
print('The Input was: ', x)
for y in x:
    if x.count(y) > 1:
        x.remove(y)
print('The Output is: ', x)

x = ["A","E","E","O","A"]
print('The Input was: ', x)
for y in x:
    if x.count(y) > 1:
        x.remove(y)
print('The Output is: ', x)

#Ans 4.1
p = []

while True:
    n = int(input('Enter the number here: '))
    
    if n != 0:
        p.append(n)
        print(p)
  
    else:
        print(p)
        break 
        
print('The final list is: ', p)

#Ans 4.2
print('The average of the input numbers is: ', sum(p)/len(p))

#Ans 5.1
numbers = []
for n in range(1,101):
    numbers.append(n)
print('The list called numbers is: ', numbers)

#Ans 5.2
squares = []
for n in numbers:
    squares.append(n)
    squares.append(n**2)
    
print('The list called squares is: ', squares)

#Ans 6
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

for x in range(6,10):
    squares[x] = x**2

print('The modified "squares" is: ', squares)

print('The value associated with the first key: ', squares.pop(1))

#Ans 7
arra = [[1,2,3,4], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
print('The original nested list is: ', arra)
for x in arra:
    x.pop()
print('The nested list after removal of last element from each sublist is: ', arra)

#Ans 8
z = {'a':100, 'b':200, 'c':300}
print('Input: ', z)
print('Output: ', sum(z.values()))

b = {'x':25, 'y':18, 'z':45}
print('Input: ', b)
print('Output: ', sum(b.values()))

#Ans 9
t_o_t = (('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'), ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'))
print('Extracting the given items: ')
print(t_o_t[0][3])
print(t_o_t[1][-2])

print('The required order: ', t_o_t[0][0], ',', t_o_t[1])

#Ans 10
lst = [2,3,5,6,7,8]

dic = {x: (x+2) for x in lst[0:4]}

print(dic)