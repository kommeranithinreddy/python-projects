#Maxvalue


A=[2,6, 9, 2,3, 65, 12,34, 98, 35, 23, 12, 87, 44,22, 57]

max_value = A[0]
for i in range(len(A)):
    if max_value < A[i]:
        max_value = A[i]
print(max_value)
