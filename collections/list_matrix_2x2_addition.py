# Adding 2X2 matrices

A = [[1,2,3],[3,4,5]]
B = [[5,5,5],[6,6,6]]
D = []
for i in range(2):
    C = []
    for j in range(3):
        C.append(A[i][j] + B[i][j])
    D.append(C)

print(D)
    
    
