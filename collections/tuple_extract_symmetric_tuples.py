'''A = [1,2,3,4,5,6]

for i in A:
    print(id(A))
    del i
    print(id(A))
    

A = "ni"

for i in A:
    print(id(A))
    print(id(A[0]))
    A = "Shubham"
    print(id(A))
    print(id(A[0]))'''

A = "nit"

for i in A:
    print(id(A))
    A = 's'
    print(id(A))
