#Bubble sort

L = [2, 3, 1, 3, 20, 12, 13, 15, 1]

print(L)

for _ in range(len(L)):
    a = 1
    for j in L:
        if j > L[a]:
            temp = L[a-1]
            L[a-1] = L[a]
            L[a] = temp
            
        a += 1
        if a>(len(L)-1):
            break

print(L)
