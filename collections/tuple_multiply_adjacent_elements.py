#Multiply Adjacent elements
Tu = (1, 5, 7, 8, 10)

NTu = ()
for i in range(len(Tu)-1):
    a = (Tu[i]*Tu[i+1],)
    NTu = NTu + a
print(NTu)

L = []
for i in range(len(Tu)-1):
    a = Tu[i]*Tu[i+1]
    L.append(a)

print(tuple(L))
