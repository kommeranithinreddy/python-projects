#Group Similar items to Dictionary Values List

L = ['apple', 'banana', 'apple', 'orange', 'banana']

d = {}

for i in L:
    if i in d:
        d[i].append(i)
    else:
        d[i] = [i]

print(d)
