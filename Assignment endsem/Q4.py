#part a.
name = input('Enter your name:') #taking name as input

age = int(input('Enter your age:')) #taking age as input

tup = (name, age) #forming the touple

print('The tuple is:', tup) #output 1

#part b.

lst = [] #taking an empty list to form the final list
#taking inputs and forming touple as done in part a
for i in range(10):
    name = input('Enter your name:')
    age = int(input('Enter your age:'))
    tup = (name, age)
    lst.append(tup) #appending the touple to the list

print('The list of tuples:', lst) #otput 2

#part c.
search = input('Enter the name you want to search:') #input the name to search

for i in lst:
    if search in i: #checking availability
        print('The age of {} is'.format(search), i[1], 'years') #printing output 3

