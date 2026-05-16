

d = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}


L = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]

OL = []

for i in L:
    c = 0
    for j in i:
        c = d[j]+c
    OL.append(c)
print(OL)
