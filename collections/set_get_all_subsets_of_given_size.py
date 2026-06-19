


s = {1, 2, 3, 4, 5}
k = 2

L = []

for i in s:
    for j in s:
        if i != j:
            if [j, i] not in L:
                L.append([i, j])

print(L)


#+==================================+


P = []
for i in s:
    for j in s:
        for k in s:
            if i != j and i != k and j != k:
                if {i, j, k} not in P:
                    P.append({i, j, k})

#print(P)

s = list({1, 2, 3, 4, 5})
Z = []
for i in range(len(s)):
    for j in range(len(s)):
        if i != j:
            if i<j:
                Z.append([s[i], s[j]])

print(Z)
