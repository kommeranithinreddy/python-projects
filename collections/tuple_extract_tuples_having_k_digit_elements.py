#Extract tuples having K digit elements

test_list = [(54, 2), (34, 55), (222, 23), (12, 45, 53), (78, )]
K = 2 
L = []
for i in range(len(test_list)):
    x = 0
    for j in range(len(test_list[i])):
        c = 1
        d = 0
        a = test_list[i][j]
        while c != 0:
            a = a//10
            d = d+1
            if a == 0:
                c = 0
        if d == K:
            x = x + 1
        if x == len(test_list[i]):
            L.append(test_list[i])

print(L)
