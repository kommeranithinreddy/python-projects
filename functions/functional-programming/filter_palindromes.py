word_list = ['kinnikinnik','detartrated','malayalam','aha', 'nithin', 'reddy']


palindrome_list = list(filter(lambda word : word == word[-1::-1], word_list))

print(palindrome_list)
