Text = input()

C = 0
D = 0
T = Text.split()
for i in T:
    for j in i:
        if '0'<=j<='9' :
            C = C+1
        if ('A'<=j<='Z' or 'a'<=j<='z'):
            D = D+1

    if C>0 and D>0:
        print(i, "Both num and char is avaiable in string")
    else:
        if C==0 and D==0:
            print(i, "Both are not avaibale")
        elif C!=0:
            print(i, "Char is not available")
        else:
            print(i, "Num is not available")
    C = 0
    D = 0
