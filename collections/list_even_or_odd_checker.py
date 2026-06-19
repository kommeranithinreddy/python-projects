#EvenOdd


A=[2, 6, 9, 2, 3, 65, 2,34, 98, 35, 23, 12, 87, 44, 22, 57]
b  = len(A)

for index in range(b):
    
    if A[index]%2 != 0:
        print(f' {A[index]} is odd')
    else:
        print(f' {A[index]} is even')
