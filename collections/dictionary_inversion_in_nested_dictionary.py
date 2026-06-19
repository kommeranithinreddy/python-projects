

d = {"a" : {"b" : {}}, "d" : {"e" : {}}, "f" : {"g" : {}}}
TO = {'b': {'a': {}}, 'e': {'d': {}}, 'g': {'f': {}}}

O ={}
for i in d:
     for j in d[i]:
         O[j] = {i:{}}
print(O)
