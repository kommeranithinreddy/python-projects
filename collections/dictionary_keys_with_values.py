d =  {'abc': [10, 30], 'bcd': [30, 40, 10]}


V = list(d.values())

S = sorted({j for i in V for j in i})

d1 = {}
for i in S:
    L = []
    for j in d:
        if i in d[j]:
            L.append(j)
            
    d1.update({i:L})

print(d1)
    
    


