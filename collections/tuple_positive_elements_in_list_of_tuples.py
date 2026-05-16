#Tuples with positive elements in List of tuples

'''Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
Output : [(4, 5, 9)] '''


T = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]

T2 = []
for i in T:
    a = 0
    for j in i:
        if j>0:
            a += 1
        if a == len(i):
           T2.append(i)
print(T2)
