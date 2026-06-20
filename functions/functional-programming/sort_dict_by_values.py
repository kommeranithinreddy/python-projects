test_dict = {'nithin':22, 'nandini' : 20, 'shubham' : 21, 'santhosh' : 24 }

sort_dict = dict(sorted(test_dict.items(), key = lambda value: value[1]))
print(sort_dict)