

#Input : test_dict = {'Gfg': { 'a' : [1, 3, 7, 8], 'b' : [4, 9], 'c' : [0, 7]}} 
#Output : {'c': {'Gfg': [0, 7]}, 'b': {'Gfg': [4, 9]}, 'a': {'Gfg': [1, 3, 7, 8]}}


ID = {'Gfg': { 'a' : [1, 3, 7, 8], 'b' : [4, 9], 'c' : [0, 7]}} 

OD = {}
for i in ID:
    for j in ID[i]:
        OD[j] = {i : ID[i][j]}

print(dict(reversed(list(OD.items()))))
