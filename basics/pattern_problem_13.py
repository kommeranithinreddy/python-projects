#pattern problem

spaces = 0
y = ' '
for i in range(5, 0, -1):
    print(spaces*y, end= '')
    
    for j in range(i):
        print('* ', end='')
        
    spaces = spaces  +1
    
    print()


#-------------------------------------------------------

sp = 4
p = ' '
for i in range(1, 6):
    for _ in range(sp):
        print(p, end='')

    for j in range(1, i+1):
        print('* ', end='')
    sp = sp-1
    print()
