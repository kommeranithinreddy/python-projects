#Pattern Problem


num = int(input("Enter any number: "))


n = num
sp = num*2 - 2
j = 2

for i in range(1, n*2):
    print('-'*sp, end = '')
    alp = 96 + num

    mid = j//2+1

    for k in range(1, j):
        print(chr(alp), end='')
        print('-', end='')

        if k >= i:
            alp = alp + 1
        else:
            alp = alp - 1


    print('-' * sp, end = '')

    if i >= n:
        sp = sp + 2
        j = j - 2 
    else:
        sp = sp - 2
        j = j + 2
    print()

