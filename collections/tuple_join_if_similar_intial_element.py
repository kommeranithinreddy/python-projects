#Join Tuples If Similar Initial Element

'''Input: [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
Output: [(5, 6, 7, 8), (6, 10), (7, 13)] 

L = [(5, 6), (5, 9), (5, 8), (6, 10), (7, 13)]

L1 = []
a = 1
i = 0
for _ in range(len(L)):
    L[i] = list(L[i])
    for j in range(a, len(L)):
        if L[i][0] == L[j][0]:
            L[i].append(L[j][1])
    L1.append(tuple(L[i]))
    del L[i]
    a = a+1
    
print(L1)'''


