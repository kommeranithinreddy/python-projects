word_list = ['nithin', 'nandini', 'shubham', 'santhosh', 'anil', 'harshith', 'nagaraju']
word_list2 = ['abcd', 'abc', 'ab', 'a']

sorted_list = sorted(word_list, key = lambda word : len(word))
sorted_list2 = sorted(word_list2, key = lambda word : len(word))

print(sorted_list)
print(sorted_list2)