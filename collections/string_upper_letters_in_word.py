#Uppercase the First and Last letter in word.


Text = input("Enter :")
L = []
T = ''
for i in Text:
    if i == ' ':
        TF = T[0].upper()
        TM = T[1:len(T)-1].lower()
        TL = T[-1].upper()
        T = TF + TM + TL
        L.append(T)
        T = ''

    else:
        T = T+i

if T != '':
    TF = T[0].upper()
    TM = T[1:len(T)-1].lower()
    TL = T[-1].upper()
    T = TF + TM + TL
    L.append(T)

Text2 = ' '.join(L)
print(L)
print(Text2)
