n = int(input())
L = 0
p = 0
cd = 0
for i in range(n):
    s = list(map(int, input().split()[:2]))
    if s[0] > s[1]:
        cd = s[0] - s[1]
        if L<cd:
            L = cd
            p = 1
    else:
        cd = s[1] - s[0]
        if L<cd:
            L = cd
            p = 2

print(p,L)
