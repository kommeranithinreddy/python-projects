def function(L = []):
    L.append(1)
    return L

A = [1,2,3,4]
print(function())
print(function())
print(function(A))
print(function())
print(function())