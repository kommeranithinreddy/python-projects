#pattern printing
sp = 4
for i in range(1, 6):
    for _ in range(sp):
        print(' ', end='')

    for j in range(1, i+1):
        if j == i:
            print(1, end=' ')
        else:
            print(j, end=' ')

    sp= sp-1
    print()
