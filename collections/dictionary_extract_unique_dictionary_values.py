d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}

V = list(d.values())

s = set()
for i in V:
    for j in i:
        if isinstance(j, int):
            s.add(j)

l = sorted(s)
print(l)

