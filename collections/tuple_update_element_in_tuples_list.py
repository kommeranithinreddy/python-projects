#Update Each Element in Tuple List

a = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]


L2 = []
for i in range(len(a)):
    L1 = []
    for j in range(len(a[i])):
        b = a[i][j]+4
        L1.append(b)
    L2.append(tuple(L1))
    

print(L2)
