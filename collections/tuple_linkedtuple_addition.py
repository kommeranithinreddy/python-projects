'''Input : test_list = [[('Gfg', 3)], [('best', 1)]] cus_eles = [1, 2] 
Output : [[('Gfg', 3, 1)], [('best', 1, 2)]] '''

test_list = [[('Gfg', 3)], [('best', 1)]]

test2=[]
for i in test_list[0]:
    i = i + (7,)
    test2.append(i)

print(test2)
