a = [1,2,3,4]

b = a


for i in range(len(a)):
    print(id(range(len(a))))
    a.append(1)

    

