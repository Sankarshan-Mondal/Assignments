
#list of lists
n = int(input('enter number of edges you want to enter:'))

graph = []#forming the empty list

for i in range(n):#choosing the number of pairs
    while True:     #restricting the number of inputs in the smaller list to two
        l = input('Enter edges:').split(' ') #taking edges as input
        if len(l)!=2:
            print('Enter two numbers')
        elif l[0]==l[1]: #not allowing duplicates
            print('Enter some different edgepoints')
        else: 
            k = [int(i) for i in l]
            if k in graph:
                print('Already taken')
            elif k[::-1] in graph:
                print('Already taken')
            else:
                graph.append(k) #appending the original list
                break
            
    # if len(l)==2:   #taking paired values as valid inputs
    #     while True:
    #         if l[0]!=l[1]:
    #             print('Enter some different edgepoints')
    #         else:
    #             break
        
            
print('The list named "graph":', graph)#output 1


#Adjacency list
#creating set because we can get the keys of the dictionary from that
set1 = []
for i in graph:
    for j in i:
        set1.append(j)
set1 = set(set1)

#print(set1) to check the keys

#creating dictionary adjlst
adjlst ={}

for k in set1:  #iterating the keys
    a = []      #forming the output list
    for i in graph:
        if k in i:
            a.append(i[1-i.index(k)]) #we are taking just the element of the list which is the output variable
    adjlst[k]=a     #adding key-value pairs to the dictionary

print('The dictionary of lists:', adjlst)#output 2
