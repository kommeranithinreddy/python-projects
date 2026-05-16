

a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]

x = 0
d = {}
e = {}
for i in a:
    d.update({b[x] : {i : a[i]}})
    e[b[x]] = {i : a[i]}
    x += 1
    

print(d, e, sep='\n')

    
