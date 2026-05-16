import math

D = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6, 'K' : 7}
K = 3
E = list(D.items())
a = len(D)/K
b = math.ceil(a)

L1 = []
x = 0
for _ in range(b):
    L = {}
    for _ in range(K):
        if x == len(E):
            break
        y,z = E[x]
        L[y] = z
        x += 1

    if L != {}:
        L1.append(L)

print(L1)


