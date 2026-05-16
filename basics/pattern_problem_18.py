sp = 4
for i in range(1, 6):
    print(' '*sp, end='')
    for j in range(1, i+1):
        if j<i:
            print(j, end=' ')
        else:
            print(1, end=' ')

    sp=sp-1
    print()
