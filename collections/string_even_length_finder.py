#Even words in string

T = input("ENTER : ")
S = input("ENTER : ")

L = []
st = ''
for i in T:
    if i != S:
        st = st+i
    else:
        L.append(st)
        st = ''

if len(st)>0:
    L.append(st)
    st = ''

for i in L:
    if len(i)%2 == 0:
        print(i)
    
