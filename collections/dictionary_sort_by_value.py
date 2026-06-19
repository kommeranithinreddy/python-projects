

a = {'apple': 5, 'banana': 2, 'cherry': 7, 'carrot' : 1, 'orange' : 10, 'mango' : 6}
b = a.items()
c = list(b)

x = 1
for i in range(len(c)-1):
    for j in range(len(c)-1):
        if c[j][x] > c[j+1][x]:
            c[j], c[j+1] = c[j+1], c[j]

print(dict(c))
