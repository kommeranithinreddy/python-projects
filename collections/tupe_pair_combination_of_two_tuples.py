#All pair combinations of 2 tuples

'''
Input : t1 = (7, 2), t2 = (7, 8) 
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)] 
'''

t1 = (7, 2)
t2 = (7, 8)

L = []
for i in t1:
    for j in t2:
        L.append((i,j))
        
for i in t2:
    for j in t1:
        L.append((i,j))

print(L)
