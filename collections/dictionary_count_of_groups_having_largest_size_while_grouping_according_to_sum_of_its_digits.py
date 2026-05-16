d = {}

n = int(input())

for i in range(1, 10):
    if i > n:
        break
    d[i]=[]
    

for i in range(1, n+1):
    a = 0
    b = i
    while b!=0:
        c = b%10
        a = a+c
        b = b//10
        if a>9:
            b = a
            a = 0
    d[a].append(i)

print(d)
'''      
a = 1
for i in range(1, n+1):
    d[a].append(i)
    a+=1
    if a>9:
        a = 1'''

v = list(d.values())


x = 0
y = 0
for i in v:
    if len(i)>x:
        x = len(i)
    if len(i) == x:
        y = y+1

print(x)
print(y)

