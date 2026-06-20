str_tuple = ('abc', 'bac', 'acb', 'aaa','acc','adc','acd')

sorted_tuple = sorted(str_tuple,key = lambda word:word[2])
print(sorted_tuple)
