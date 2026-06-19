A = input("Enter your string: ")
X = input("Enter split character: ")
L = []
B = ''

for i in A:
    if i != X:
        B = B + i
    elif B != '':
        L.append(B)
        B = ''
if B != '':
    L.append(B)
    
print(A, L, sep ='\n')
