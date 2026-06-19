#Create a List of Tuples with Numbers and Their Cubes - Python


L1 = map(int, input().split())

L2 = []

for i in L1:
    t1 = i, i**3
    L2.append(t1)

print(L2)
