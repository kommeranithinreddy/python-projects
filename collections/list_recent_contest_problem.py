n = int(input())

for i in range(n):
    c1 = 0
    c2 = 0
    L = list(map(str, input().split()))
    print(L)
    for V in L:
        if V == 'START38':
            c1 += 1
        elif V == 'LTIME108':
            c2 += 1
    print(c1, c2)
