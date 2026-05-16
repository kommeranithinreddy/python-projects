# cook your dish here
inpu = list(map(int, input().split()[:4]))

b = inpu

c = 0
for v in inpu:
    if v>=10:
        c = c+1
    
print(c)
