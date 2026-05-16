#Remove Tuples from the List having every element as None

'''Input : test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 
Output : [(None, 2), (3, 4), (12, 3)] '''



t = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]


p = []
for i in t:
    a = 0
    for j in i:
        if j == None:
            a = a+1
    if a != len(i):
        p.append(i)
print(p)



b = 0
c = len(t)
while b < c:
    d = 0
    x = 0
    f = len(t[b])
    while d<f:
        if t[b][d] == None:
            x+=1
        if x==len(t[b]):
            del t[b]
            b = b-1
            c = c-1
        d+=1
    b += 1
print(t)
            
