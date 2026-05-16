n = int(input())
A = []
for i in range(n):
    p1, p2 = map(int, input().split())
    if p1>p2:
        p = [p1-p2, 1]
        A.append(p)
    else:
        p=[p2-p1, 1]
        A.append(p)

M = max(A)
print(M[1], M[0])
