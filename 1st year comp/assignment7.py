#CS1101
#Assignment 7_2021-batch

#Ans 1
print('=====Calculator=====\n', '1 - Addition\n', '2 - Substraction\n', '3 - Multiply\n', '4 - Division\n', 'Any other number to exit')
x = int(input('Enter your choice: '))

if x in range(1,5): 
    
    print('Enter the two operands')
    y = float(input('Enter 1st operand: '))
    z = float(input('Enter 2nd operand: '))
    
    while x == 1:
       print('Result: ', y+z)
       print('=====Calculator=====\n', '1 - Addition\n', '2 - Substraction\n', '3 - Multiply\n', '4 - Division\n', 'Any other number to exit')
       x = int(input('Enter your choice: '))
       print('Enter the two operands')
       y = float(input('Enter 1st operand: '))
       z = float(input('Enter 2nd operand: '))

    while x == 2:
        print('Result: ', y-z)
        print('=====Calculator=====\n', '1 - Addition\n', '2 - Substraction\n', '3 - Multiply\n', '4 - Division\n', 'Any other number to exit')
        x = int(input('Enter your choice: '))
        print('Enter the two operands')
        y = float(input('Enter 1st operand: '))
        z = float(input('Enter 2nd operand: '))

    while x == 3:
        print('Result: ', y*z)
        print('=====Calculator=====\n', '1 - Addition\n', '2 - Substraction\n', '3 - Multiply\n', '4 - Division\n', 'Any other number to exit')
        x = int(input('Enter your choice: '))
        print('Enter the two operands')
        y = float(input('Enter 1st operand: '))
        z = float(input('Enter 2nd operand: '))

    while x == 4:
        print('Result: ', y/z)
        print('=====Calculator=====\n', '1 - Addition\n', '2 - Substraction\n', '3 - Multiply\n', '4 - Division\n', 'Any other number to exit')
        x = int(input('Enter your choice: '))
        print('Enter the two operands')
        y = float(input('Enter 1st operand: '))
        z = float(input('Enter 2nd operand: '))

else:
    print('Exiting...\n')
    
    
#Ans 2
print('Enter the points with a space between the coordinates')
#Input:
x = [float(num) for num in input('Enter point 1: ').split(' ', 1)]
y = [float(num) for num in input('Enter point 2: ').split(' ', 1)]

z = (x[0] - y[0])**2 + (x[1] - y[1])**2
#Output:
print('\nThe distance between them: ', z**(1/2))
print('\n')

#Ans 3
#Input:
x = [int(num) for num in input('Enter the number of wins, loses, draws (space seperated): ').split(' ', 2)]

z = x[0]*2 + x[1]*0 + x[2]*1
#Output:
print('\nThe point of the team is: ', z)


#Ans 4
#Input:
print('\nUse capital letters to denote bases')
x = input('DNA string: ')

z = x.replace('T', 'U')

#Output:
print('\nThe RNA string is: ', z)
print('\n')


#Ans 5
#Input
x = input('Enter your DNA sequence here: ')
#Output
print('A : ', x.count('A'), 'C : ', x.count('C'), 'G : ', x.count('G'), 'T : ', x.count('T'))
print('\n')

#Ans 6
#Input:
x = [str(y) for y in input('Enter the bunch of words here: ').split(' ')]

x = set(x)
x = list(x)
x.sort()
x = ' '.join(str(y) for y in x)

#Output:
print(x)
print('\n')


#Ans 7
lst = ['I','think','therefore','I', 'am','said','Rene','Descartes']
dct = {'Rene' : 0, 'Descartes' : 1, 'I' : 2, 'think': 3}

#Input:
i = input('Enter the word, K: ')

#Output:
if i in lst:
    if i in dct:
        print('Value of', i, 'in dictionary is ', dct[i])
    else:
        print('Key:', i, 'not found in dictionary')
else:
    print('Key:', i, 'not found in either list or dictionary')

