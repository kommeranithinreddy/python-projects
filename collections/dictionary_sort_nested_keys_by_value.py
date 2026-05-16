

d = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
     'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
     'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}
d1 = {}

for i in d:
    L = list(d[i].items())
    for j in range(len(L)):
        for k in range(len(L)):
            if L[j][1] > L[k][1] and j < k:
                L[j], L[k] = L[k], L[j]
    d2 = dict(L)
    d1[i] = d2

print(d1)
