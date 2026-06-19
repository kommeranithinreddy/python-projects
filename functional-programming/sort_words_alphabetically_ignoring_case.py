char_tuple = ('banana', 'Apple', 'Box', 'aeroplane', 'cat', 'zip', 'Zeebra')

sort_tuple = sorted(char_tuple, key = lambda char : char.lower())

print(sort_tuple)