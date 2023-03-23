
#list of lists
n = int(input('enter number of edges you want to enter:'))

graph = []
for i in range(n):
    l = input('Enter edges:').split(' ')
    if len(l)==2:
        l = [int(i) for i in l]
        graph.append(l)
    else:
        print('Enter only two numbers')
        l = input('Enter edges:').split(' ')

print(graph)

#creating dictionary

set1 = []
for i in graph:
    for j in i:
        set1.append(j)
set1 = set(set1)

print(set1)

adjlst ={}

for i in graph:
    #j = []
    for j in i:
        for

