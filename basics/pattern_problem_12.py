#pattern problem


x = ' '
y = 4
for i in range(1, 6):
    print(x*y, end =' ')
    print(i*'* ', end=' ')
    print(x*y, end=' ')
    y = y-1
    print()

