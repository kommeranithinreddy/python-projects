def str_reverse(string):
    for index in range(len(string)-1, -1, -1):
        yield string[index]

name = str_reverse('Reddy')


for i in name:
    print(i, end='\t')