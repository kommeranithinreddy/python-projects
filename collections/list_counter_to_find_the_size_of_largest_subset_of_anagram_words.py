

i = 'ant magenta magnate tan gnamate'

L =i.split()


L1 = []
L2 = []
L3 = []
for i in L:
    if i not in L2:
        L1.append(i)
        L2.append(i)
    for j in L:
        c = 0
        if len(i) == len(j) and i != j:
            for k in i:
                if k in j:
                    c = c+1
            if len(i) == c:
                L1.append(j)
    if j not in L2:
        L3.append(L1)
        L2.append(j)
        L1 = []
print(L3)
print(L2)
        
        
                
