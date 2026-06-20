words_list = ['nithin', 'apple', 'banana', 'orange', 'eye', 'item', 'elephant']

vowel_word_list = list(filter(lambda word: word[0] in 'AEIOUaeiou', words_list))

print(vowel_word_list)