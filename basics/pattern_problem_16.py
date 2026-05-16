sp = 4
for i in range(1, 5):
    print(sp* ' ', end='')
    k = 1
    for j in range(1, i*2):
        if j>=i:
            print(k, end=' ')
            k = k-1
        else:
            print(k, end=' ')
            k = k+1

    sp = sp-1
    print()
