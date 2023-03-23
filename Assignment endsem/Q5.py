
#taking input
r = int(input('Enter a positive number:'))


#making an empty list
s=[]

#the working code
if r>0:
    #We use the simple property that (a+b)^3 > a^3 + b^3.
    #Therefore, we will always have r > (a^3+b^3)^(1/3).
    for i in range(1, int(r**(1/3))+1): #checking values of i
        for j in range(1, int(r**(1/3))+1): #checking values of j
            if i<j: #applying condition to prevent repetetion
                if r == i**3 + j**3: #applying the relation
                    z = (i,j) #forming the tuple
                    s.append(z) #appending the tuple to s
else:
    print('Enter a positive number')   

#the code for generating the output
if len(s)>0: #determining the Ramanujan number by size of list s
    print(r, 'is a Ramanujan number') 
    print('The numbers whose cubes add up are:', s)
else:
    print(r,'is not a Ramanujan number')  
