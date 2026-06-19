d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

L = sorted(d.keys())
d1 = {}

for i in d:
    d[i].sort()
    
for i in L:
    d1[i]=d[i]

print(d1)
O = {'a': [4, 19], 'b': [10, 12], 'c': [3]}
print(d1 == O)
