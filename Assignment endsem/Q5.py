
#taking input
r = int(input('Enter a number:'))


#making an empty list
s=[]

#the working code
if r>0:
    #We use the simple property that (a+b)^3 > a^3 + b^3.
    #Therefore, we will always have r > (a^3+b^3)^(1/3).
    for i in range(1, int(r**(1/3))+1): 
        for j in range(1, int(r**(1/3))+1):
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
