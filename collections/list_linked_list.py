#Creating 3X3 Matrices using LinkedList

A = []
for i in range(3):
    L = []
    for  j in range(3):
        inp = int(input(f'insert your number in list of [{i}], [{j}]: '))
        L.append(inp)
    A.append(L)

print(A)



for b in A:
    v = 0 
    for c in b:
        v = v + c

    print(v, v/3)
    
        


