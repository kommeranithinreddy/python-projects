#Transpose 3X3

A = [[1,2,3],[4,5,6],[7,8,9]]


for i in range(3):
    b = 0
    for _ in range(9):
        if b >= 3:
            b = 0
        if b == i:
            print(A[i][b], end=' ')
        b = b+1

            
    print()
        
