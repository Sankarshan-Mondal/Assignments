#part a.
name = input('Enter your name:')

age = int(input('Enter your age:'))

tup = (name, age)

#part b.

lst = []
for i in range(3):
    name = input('Enter your name:')
    age = int(input('Enter your age:'))
    tup = (name, age)
    lst.append(tup)


#part c.
search = input('Enter the name you want to search:')

for i in lst:
    if search in i:
        print('The age of {} is'.format(search), i[1], 'years')

