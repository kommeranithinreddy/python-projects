y = ' '
s = 4
for i in range(5):
    print(s*y, end='')

    for j in range(1, i+1):
        print(j, end=' ')

    print(1, end='')
    s= s-1
    print()
