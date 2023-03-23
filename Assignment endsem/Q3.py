
#list of lists
n = int(input('enter number of edges you want to enter:'))

graph = []

for i in range(n):
    l = input('Enter edges:').split(' ')
    if len(l)==2:
        k = [int(i) for i in l]
        graph.append(k)
    else:
        print('Enter only two numbers')
        l = input('Enter edges:').split(' ')


print(graph)

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

print('The dictionary of lists:', adjlst)
