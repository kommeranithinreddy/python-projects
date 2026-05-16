sp = 3
j = 1
for i in range(1, 8):
    print(sp*' ', end='')
    for k in range(1, j+1):
        print(k, end=' ')

    if i <= 3:
        sp = sp - 1
        j = j + 1
    elif i > 3:
        sp = sp + 1
        j = j - 1
    print()
