
for i in range(1, 5):
    k = 1
    for j in range(1, i*2):
        if j>=i:
            print(k, end='')
            k = k-1
        else:
            print(k, end='')
            k = k+1
    print()
