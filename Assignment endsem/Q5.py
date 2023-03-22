
#taking input
r = int(input('Enter a number:'))


#making an empty list
s=[]

#the working code
if r>0:
    for i in range(1,r):
        for j in range(r):
            if i<j:
                if r == i**3 + j**3:
                    z = (i,j)
                    s.append(z)     
else:
    print('Enter a positive number')   

#the code for generating the output
if len(s)>0:
    print(r, 'is a Ramanujan number') 
    print(s)
else:
    print(r,'is not a Ramanujan number')  
