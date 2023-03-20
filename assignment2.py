
#Ans 1
x = 'Sankarshan Mondal'
for i in range(1,16):
    print(i, x)
    
#Ans 2
for j in range(1,16):  # only serial numbers with multiple of 3 are being selected.
    if j % 3 == 0:
        print(j, x)
        
        
#Ans 3
p = 'abcdefghijkl'

x = len(p)

for y in range(x):
    print(p[y:x])


    
#Ans 4

c = [0,3,1,2,8,9,0,4,7]

maximum1 = sorted(c)
print('Maximum value without using max command: ', maximum1[len(maximum1)-1])

d = [0,-1,-3,-4,3,8,9,11,-2]

maximum2 = sorted(d)
print('Maximum value without using max command: ', maximum2[len(maximum2)-1])

#Ans 5.

p = [0, 3, 1, 2, 8, 9, 0, 4, 7]

maximum3 = sorted(p)
print('The maximum without using max command: ', maximum3[len(maximum3)-1])
print('The position of the maximum element is: ', p.index(maximum3[len(maximum3)-1]))
print('The minimum without using min command: ', maximum3[0])
print('The position of the minimun element is: ', p.index(maximum3[0]))

print('The maximum using max command: ', max(p))
print('The minimum using min command: ', min(p))

q = [0, -1, -3, -4, 3, 8, 9, 11, -2]

maximum4 = sorted(q)
print('The maximum without using max command: ', maximum4[len(maximum4)-1])
print('The position of the maximum element is: ', q.index(maximum4[len(maximum4)-1]))
print('The minimum without using min command: ', maximum4[0])
print('The position of the minimum element is: ', q.index(maximum4[0]))

print('The maximum using max command: ', max(q))
print('The minimum using min command: ', min(q))
   

#Ans 6.
name = 'sankarshan'
year = '2021'
cid = 'MS'
sid = '1234'

b = [name,'-', year[2]+year[3],'-', cid,'-', sid, '@iiserkol.ac.in']

x = ''.join(b)

print('The email id generated is:', x)

#Ans 7
str1 = '123'
str2 = '234'
str3 = '456'
lst = [str1, str2, str3]
a = int(str1) + int(str2) + int(str3)

b = int(str1) * int(str2) * int(str3)
print('Sum of the numbers: ', a)
print('Product of the numbers: ', b)
print('Average of the numbers: ', a/len(lst))

#Ans 8


m = [x for x in range(1,6)]
print('The numbers in loop are: ', m)

print('sum of numbers in m is- ', sum(m))

    
#Ans 9. a)

numlist = [39, 94, 59, 85, 36, 32, 97, 44, 86, 98]

#Ans 9. b)

numlist.sort(reverse = True)

print('The scores in descending order are: ', numlist)

#Ans 9. c)

for x in range(len(numlist)):
    if numlist[x] < 45:
        numlist[x] += 5
        
print('The scores after adding grace marks are: ', numlist)
    
#Ans 9. d)

list1 = []
for x in range(len(numlist)):
    if numlist[x] < 50:
     list1.append(numlist[x])
print('The scores below 50 are: ', list1)
print('Number of students who have failed are: ', len(list1))
        

#Ans 10. a)

n = [5,6,-8,9,56,2,0,-3,-4,8]

print('The entire list: ', n)

#Ans 10. b)

n.sort()
print('The sorted list is: ', n)

#Ans 10. c)

n.pop(9) #removing the maximum value
n.pop(0) #removing the minimum value

print('The list without the maximum and minimum value: ', n)
