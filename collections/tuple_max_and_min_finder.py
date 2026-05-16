Tup = (1, 1, 1,1,1)
K = 2

List = sorted(Tup)
Mi = []
Ma = []
for i in List:
    if Mi == []:
        Mi.append(i)
    elif len(Mi)<K:
        if Mi[len(Mi)-1] < i:
            Mi.append(i)
            
    if len(Ma)< K:
        Ma.append(i)
    elif min(Ma)<i:
        if i not in Ma:
            Ma.remove(min(Ma))
            Ma.append(i)       
print(Mi)
print(Ma)



Mini = []
Maxi = []
a = -1

for i in range(len(List)):
    b = a-i
    if i == 0:
        Mini.append(List[i])
    elif len(Mini)<K:
        if Mini[len(Mini)-1] < List[i]:
            Mini.append(List[i])
            
    if Maxi == []:
        Maxi.append(List[b])
    elif len(Maxi)<K:
        if Maxi[len(Maxi)-1] > List[b]:
            Maxi.append(List[b])
print(Mini)
print(Maxi)


    
        
