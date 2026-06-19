#All elements divisible by K from a list of tuples

'''
Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6 
Output : [(6, 24, 12), (60, 12, 6)] '''

T = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = 6

T2 = []
for i in T:
    a = 0
    for j in i:
        if j%K == 0:
            a += 1
        if a == len(i):
            T2.append(i)
print(T2)
