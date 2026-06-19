

d = {'Gfg' : [8], 'best' : [5]}
Output = {'Gfg': 17, 'best': 18} 


L = list(d.items())
d1={}
for i in L:
    a, b = i
    d1[a] = sum(b)

print(d1)

