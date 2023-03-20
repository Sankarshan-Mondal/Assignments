#CS1101
#Assignment 8_2021-batch

#Ans 1
x = str(input('Enter a mRNA: '))
s = []
for i in range(len(x)):
    if i != 0:
        if i%3 == 0:
            s.append(x[i-3] + x[i-2] + x[i-1])
print('The Codons are: ', s)

p = []
for i in ['A','U','G','C']:
    for j in ['A','U','G','C']:
        for k in ['A','U','G','C']:
            p.append(i+j+k)
#print(p)

for x in p:
    if x in s:
        print('freq_'+str(x),'=', s.count(x)/len(s))

#Ans 2
x = str(input('Enter a mRNA: '))
s = []
for i in range(len(x)):
    if i != 0:
        if i%3 == 0:
            s.append(x[i-3] + x[i-2] + x[i-1])
print('The Codons are: ', s)

p = {'AAA':'K', 'AAU':'N', 'AAG':'K', 'AAC':'N', 'AUA':'I', 'AUU':'I', 'AUG':'M', 'AUC':'I', 'AGA':'R', 'AGU':'S', 'AGG':'R', 'AGC':'S', 'ACA':'T',
     'ACU':'T', 'ACG':'T', 'ACC':'T', 'UAA':'', 'UAU':'Y', 'UAG':'', 'UAC':'Y', 'UUA':'L', 'UUU':'F', 'UUG':'L', 'UUC':'F', 'UGA':'', 'UGU':'C', 
     'UGG':'', 'UGC':'C', 'UCA':'S', 'UCU':'S', 'UCG':'S', 'UCC':'S', 'GAA':'E', 'GAU':'D', 'GAG':'E', 'GAC':'D', 'GUA':'V', 'GUU':'V', 'GUG':'V', 
     'GUC':'V', 'GGA':'G', 'GGU':'G', 'GGG':'G', 'GGC':'G', 'GCA':'A', 'GCU':'A', 'GCG':'A', 'GCC':'A', 'CAA':'Q', 'CAU':'H', 'CAG':'Q', 'CAC':'H',
     'CUA':'L', 'CUU':'L', 'CUG':'L', 'CUC':'L', 'CGA':'R', 'CGU':'R', 'CGG':'R', 'CGC':'R', 'CCA':'P', 'CCU':'P', 'CCG':'P', 'CCC':'P'}


q = []
for i in s:
      q.append(p[i])
      if p[i] == '':
          break
r = ''.join(q)
print('The protein sequence is: ', r)


#Ans 3
import math
x = float(input('Enter the readius: '))

a = (4*math.pi/3)*x**3

e = round(a, 1)
b = round(a, 2)
c = round(a, 3)
d = round(a, 4)

print('The volume (upto 1 decimal place) is: ', e)
print('The volume (upto 2 decimal places) is: ', b)
print('The volume (upto 3 decimal places) is: ', c)
print('The volume (upto 4 decimal places) is: ', d)


#Ans 4
try:
    x = float(input('Enter any number: '))
    print()
    print('The entered number is positive.\n'+'The square root of the entered number is: ', round(x**(1/2) , 3))
except:
    print('The number entered is negative, hence it does not have a real square root')
print('Thank you')


