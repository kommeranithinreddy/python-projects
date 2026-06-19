

L = ["Gfg", "is", "Best"]
d = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
K = 0 

for i in d:
    L[L.index(i)] = d[i][K]
print(L)
